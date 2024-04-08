def is_recorded(recorder, class_, method_name):
    for lines in recorder.get_data().values():
        for line_records in lines.values():
            if (class_, method_name) in line_records.keys():
                return True

    return False
