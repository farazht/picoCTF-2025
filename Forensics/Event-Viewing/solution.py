from Evtx import Evtx

def parse_evtx(input_file):
    """Parses a Windows Event Log (.evtx) file and prints its contents."""
    with evtx(input_file) as log:
        for record in log.records():
            print(f"Event Record ID: {record.event_record_id}")
            print(f"Timestamp: {record.timestamp}")
            print(f"Data: {record.data}")
            print("-" * 40)

if __name__ == "__main__":
    input_file = "Windows_Logs.evtx"
    parse_evtx(input_file)
