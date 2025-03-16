## Event-Viewing

In this challenge, we're given a Windows Event Log (`.evtx`) file, which contains a record of events that occurred the Windows system of a hypothetical coworker. This employee installed software using an installer they downloaded online, ran it, and now their computer shuts down immediately after booting up. By finding evidence for these events in the log, we're able to reconstruct the flag.

Unfortunately for me, I don't have a Windows computer available at the moment. I tried using `python-evtx` to parse the log file, but it didn't work. Instead, I installed a command-line tool which allowed me to dump the contents of the log file into a JSON file. The commands I used were:

```bash
brew install evtx

evtx_dump -o json Windows_Logs.evtx > evtx.json
```
This command created a [JSON file](./Windows_Logs.json) with the contents of the log file, which ended up being over **400,000 lines long**.

Now, I was able to search for the events I needed to find. I first looked for the first event, which was the installation of the software. I tried filtering for various terms such as `download`, `software`, `install`, `installer`, and I found the first piece of evidence pretty quickly:

```json
{
  "Event": {
    "#attributes": {
      "xmlns": "http://schemas.microsoft.com/win/2004/08/events/event"
    },
    "System": {
      "Provider": {
        "#attributes": {
          "Name": "MsiInstaller"
        }
      },
      "EventID": {
        "#attributes": {
          "Qualifiers": 0
        },
        "#text": 1033
      },
      "Version": 0,
      "Level": 4,
      "Task": 0,
      "Opcode": 0,
      "Keywords": "0x80000000000000",
      "TimeCreated": {
        "#attributes": {
          "SystemTime": "2024-07-15T15:55:57.729798Z"
        }
      },
      "EventRecordID": 2373,
      "Correlation": null,
      "Execution": {
        "#attributes": {
          "ProcessID": 0,
          "ThreadID": 0
        }
      },
      "Channel": "Application",
      "Computer": "DESKTOP-EKVR84B",
      "Security": {
        "#attributes": {
          "UserID": "S-1-5-21-3576963320-1344788273-4164204335-1001"
        }
      }
    },
    "EventData": {
      "Data": {
        "#text": [
          "Totally_Legit_Software",
          "1.3.3.7",
          "0",
          "0",
          "cGljb0NURntFdjNudF92aTN3djNyXw==",
          "(NULL)",
          ""
        ]
      },
      "Binary": "7B33443343333833332D444544362D343032322D423541312D4537463337373839433339307D3030303037363533376239373032333966396130373530633431623838363466646163393030303030303030"
    }
  }
}
```

This event shows that the software `Totally_Legit_Software` was installed on the system. The flag is in the `Data` field, and it's encoded in base64. Decoding it gives us the first part of the flag:

`picoCTF{Ev3nt_vi3wv3r_`

Next, I tried to find evidence of the user running the software. Filtering for any logs where `Totally_Legit_Software` was part of the process, I found the following event:

```json
{
  "Event": {
    "#attributes": {
      "xmlns": "http://schemas.microsoft.com/win/2004/08/events/event"
    },
    "System": {
      "Provider": {
        "#attributes": {
          "Name": "Microsoft-Windows-Security-Auditing",
          "Guid": "54849625-5478-4994-A5BA-3E3B0328C30D"
        }
      },
      "EventID": 4657,
      "Version": 0,
      "Level": 0,
      "Task": 12801,
      "Opcode": 0,
      "Keywords": "0x8020000000000000",
      "TimeCreated": {
        "#attributes": {
          "SystemTime": "2024-07-15T15:56:19.103196Z"
        }
      },
      "EventRecordID": 168656,
      "Correlation": null,
      "Execution": {
        "#attributes": {
          "ProcessID": 4,
          "ThreadID": 1084
        }
      },
      "Channel": "Security",
      "Computer": "DESKTOP-EKVR84B",
      "Security": null
    },
    "EventData": {
      "SubjectUserSid": "S-1-5-21-3576963320-1344788273-4164204335-1001",
      "SubjectUserName": "user",
      "SubjectDomainName": "DESKTOP-EKVR84B",
      "SubjectLogonId": "0x5a428",
      "ObjectName": "\\REGISTRY\\MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",
      "ObjectValueName": "Immediate Shutdown (MXNfYV9wcjN0dHlfdXMzZnVsXw==)",
      "HandleId": "0x208",
      "OperationType": "%%1904",
      "OldValueType": "-",
      "OldValue": "-",
      "NewValueType": "%%1873",
      "NewValue": "C:\\Program Files (x86)\\Totally_Legit_Software\\custom_shutdown.exe",
      "ProcessId": "0x1bd0",
      "ProcessName": "C:\\Program Files (x86)\\Totally_Legit_Software\\Totally_Legit_Software.exe"
    }
  }
}
```

This event shows us that the user `user` ran the software `Totally_Legit_Software` on the system. The flag is in the `ObjectValueName` field, and it's encoded in base64 again. Decoding it gives us the second part of the flag:

`1s_a_pr3tty_us3ful_`

Finally, I had to find evidence of the final part of the challenge description: *"every time they bootup and login to their computer, a black command prompt screen quickly opens and closes and their computer shuts down instantly"*

I initially tried filtering by relevant terms naively as I had before, but after searching for a while, to no avail, I decided to follow the advice of the hint: *"Try to filter the logs with the right event ID"*.

I found an EventID that seemed like the most likely candidate - here's the description:

### Event ID 1074: System has been shutdown by a process/user.
| | |
| --- | --- |
| Description | This event is written when an application causes the system to restart, or when the user initiates a restart or shutdown by clicking Start or pressing CTRL+ALT+DELETE, and then clicking Shut Down. |
| Category | System |
| Subcategory | Startup/Shutdown |

After looking through some of the results where `EventID = 1074`, I found the following event:

```json
{
  "Event": {
    "#attributes": {
      "xmlns": "http://schemas.microsoft.com/win/2004/08/events/event"
    },
    "System": {
      "Provider": {
        "#attributes": {
          "Name": "User32",
          "Guid": "{b0aa8734-56f7-41cc-b2f4-de228e98b946}",
          "EventSourceName": "User32"
        }
      },
      "EventID": {
        "#attributes": {
          "Qualifiers": 32768
        },
        "#text": 1074
      },
      "Version": 0,
      "Level": 4,
      "Task": 0,
      "Opcode": 0,
      "Keywords": "0x8080000000000000",
      "TimeCreated": {
        "#attributes": {
          "SystemTime": "2024-07-15T17:01:05.393583Z"
        }
      },
      "EventRecordID": 3801,
      "Correlation": null,
      "Execution": {
        "#attributes": {
          "ProcessID": 432,
          "ThreadID": 3496
        }
      },
      "Channel": "System",
      "Computer": "DESKTOP-EKVR84B",
      "Security": {
        "#attributes": {
          "UserID": "S-1-5-21-3576963320-1344788273-4164204335-1001"
        }
      }
    },
    "EventData": {
      "param1": "C:\\Windows\\system32\\shutdown.exe (DESKTOP-EKVR84B)",
      "param2": "DESKTOP-EKVR84B",
      "param3": "No title for this reason could be found",
      "param4": "0x800000ff",
      "param5": "shutdown",
      "param6": "dDAwbF84MWJhM2ZlOX0=",
      "param7": "DESKTOP-EKVR84B\\user"
    }
  }
}
```

This event details the shutdown of the system by the user `user`. The flag is in the `param6` field, and it's encoded in base64. Decoding it gives us the final part of the flag:

`t00l_81ba3fe9}`

Putting all the parts together, we get the flag:

`picoCTF{Ev3nt_vi3wv3r_1s_a_pr3tty_us3ful_t00l_81ba3fe9}`