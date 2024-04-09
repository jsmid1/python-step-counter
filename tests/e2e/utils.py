def is_recorded(recorder, module, class_, method_name):
    for lines in recorder.get_data().values():
        for line_records in lines.values():
            if (module, class_, method_name) in line_records.keys():
                return True

    return False
