import os
import re
# import shutil

#ключі папок є назвами папок, які створює функція create_folders_from_list
extensions = {
    'images': ['jpeg', 'png', 'jpg', 'svg'],
    'video': ['avi', 'mp4', 'mov', 'mkv'],
    'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'],
    'audio': ['mp3', 'ogg', 'wav', 'amr'],
    'archives': ['zip', 'gz', 'tar'],
    'non type extension': []
}

main_path = r'C:\best_folder\папка'

"""
функція сортування проходить за допомогою методу os.walk проходить через всі файли, отримуючи їх розширення, поділяючи їх на ім'я і розширення
потім, отримуючи данні значень словника ми порівнюємо розширення файлу та значення ключа, і за допомогою методу os.rename переносимо файл в 
папку, назва якого = ключу відповідного розширення
"""

def sort_path(folder_path):
    ext_list = list(extensions.items())
    for root, dirs, files in os.walk(folder_path):
        file_paths = [os.path.join(root,n) for n in files] #створюємо повний шлях до кожного файлу.


        for file_path in file_paths:
            extension = file_path.split('.')[-1] #розширення окремо
            file_name = file_path.split('\\')[-1] #назва файлу окремо
            # додано для відладки
            print(f"File path: {file_path}, extension: {extension}")

            for dict_key_int in range(len(ext_list)):
                if extension in list(ext_list[dict_key_int][1]):#за індексом визначаємо, що первіряємо розширення файлу і аргументи словника
                    print(f'Moving {file_name} in {ext_list[dict_key_int][0]} folder\n')
                    os.rename(file_path, f'{main_path}\\{ext_list[dict_key_int][0]}\\{file_name}')#переносимо файл в папку, назва якої відповідає ключу словника


#якщо папки не існує, то функція створює її
def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')

"""
фунція normilze оптимізує назви файлів. приймає на вхід рядок з назви файлу та повертає відформатований рядок,
перекладає букви з кирилиці на латиницю та всі символи окрім букв та цифр на "_'
"""

def normalize(text):
# Словник для транслітерації кирилічних символів
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ie', 'ж': 'zh', 'з': 'z',
        'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
        'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
        'ю': 'iu', 'я': 'ia', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'H', 'Ґ': 'G', 'Д': 'D', 'Е': 'E', 'Є': 'Ye',
        'Ж': 'Zh', 'З': 'Z', 'И': 'Y', 'І': 'I', 'Ї': 'Yi', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
        'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch',
        'Ш': 'Sh', 'Щ': 'Shch', 'Ь': '', 'Ю': 'Yu', 'Я': 'Ya'
    }
    # заміна кириличних символів на латиницю
    for key, value in translit_dict.items():
        text = text.replace(key, value)

    # заміна всіх символів, крім літер латинського алфавіту та цифр, на символ '_'
    text = re.sub(r'[^a-zA-Z0-9]+', '_', text)
    return text

# #Перейменовує файли та папки в заданій папці з використанням функції normalize.
# def rename_files(folder_path):
#
#     # отримуємо назви файлів та папок
#     file_names = [i.name for i in os.scandir(folder_path) if i.is_file()]
#
#     #переіменовуємо файли використовуючи функцію normalize
#     for file_name in file_names:
#         file_path = os.path.join(folder_path, file_name)
#         file_ext = os.path.splitext(file_name)[1]  # отримуємо розширення файлу
#         new_file_name = normalize(os.path.splitext(file_name)[0]) + file_ext #до нової назви додаємо розширення
#         os.rename(file_path, os.path.join(folder_path, new_file_name))

if __name__ == "__main__":
    # rename_files(main_path)
    create_folders_from_list(main_path, extensions)
    sort_path(main_path)

