import module_view as view
import module_ie_data as mied
import module_data_modification as mdm

data = []
file_name = 'phonebook'

def tg_start():
    global data
    data = mied.read_from_file(file_name)
    mdm.sort_data(data)

def tg_show_menu():
    return view.tg_show_menu()

def tg_print_records():
    global data
    return view.tg_print_records(data)

def tg_search_records():
    title = 'Выполнение поиска, укажите маску поиска: '
    choice = view.get_data(title)
    filtered_data = mdm.search_record(choice, data)
    mdm.sort_data(filtered_data)
    view.print_records(filtered_data)


def start():
    global data
    data = mied.read_from_file(file_name)
    mdm.sort_data(data)
    view.print_records(data)
    while True:
        command = view.show_menu()
        if command == '0':
            break
        elif command == '1':
            title = 'Выполнение поиска, укажите маску поиска: '
            choice = view.get_data(title)
            filtered_data = mdm.search_record(choice, data)
            mdm.sort_data(filtered_data)
            view.print_records(filtered_data)
            view.print_message('Для сброса фильтра поиска, сделайте поиск по пустому значению!')
        elif command == '2':
            title = 'Добавить новую запись. Задайте данные новой записи:'
            view.print_message(title)
            new_record = view.add_new_record()
            mdm.add_new_record(new_record, data)
            mdm.sort_data(data)
            view.print_records(data)
        elif command == '3':
            if len(data) == 0:
                view.print_message('Справочник пуст, прежде чем редактировать, добавьте хотя бы одну запись.')
                continue
            title = 'Редактировать указанную запись, укажите ID записи: '
            choice = view.get_data(title)
            record_for_edit = mdm.get_record(choice, data)
            if record_for_edit is not None:
                record_for_edit = view.edit_record(record_for_edit)
                mdm.delet_record(choice, data)
                mdm.add_new_record(record_for_edit, data)
            mdm.sort_data(data)
            view.print_records(data)
        elif command == '4':
            if len(data) == 0:
                view.print_message('Справочник пуст, прежде чем удалять, добавьте хотя бы одну запись.')
                continue
            title = 'Удалить указанную запись, укажите ID записи: '
            choice = view.get_data(title)
            mdm.delet_record(choice, data)
            mdm.sort_data(data)
            view.print_records(data)
        elif command == '5':
             mied.save_into_file(file_name, data)
             view.print_message('Изменения сохранены.')
        elif command == '6':
             mied.export_to_jison(file_name, data)
             view.print_message('Данные экспортированы.')
        elif command == '7':
             mied.export_to_xml(file_name, data)
             view.print_message('Данные экспортированы.')
        else:
            view.print_message('Выброна не верная команда, повторите выбор!')

