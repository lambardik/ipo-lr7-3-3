import json
count = 0
num = 0
with open("dump.json", "r",   encoding = "utf-8") as file:
    read_content = file.read()
    no_json = json.loads(read_content)
    for item in no_json:
        num += 1
while True:
    print("1. Вывести все записи")
    print("2. Вывести запись по полю")
    print("3. Добавить запись")
    print("4. Удалить запись по полю")
    print("5. Выйти из программы")
    punkt = int(input("Выберете пункт: "))
    with open("dump.json", "r",   encoding = "utf-8") as file:
        read_content = file.read()
        no_json = json.loads(read_content)
    if punkt == 1:
        count += 1
        for item in no_json:
            print("=" * 20, f"Номер записи: {item['id']}", "=" * 20)
            print(f"Общее название звезды: {item['name']} \n Название созвездия: {item['constellation']} \n Можно ли увидеть звезду без телескопа: {item['is_visible']} \n Солнечный радиус звезды: {item['radius']}")
    elif punkt == 2:
        count += 1
        record = input("Введите поле: ")
        found = False
        for item in no_json:
            if item["id"] == record:
                print("=" * 20, f"Номер записи: {item['id']}", "=" * 20,)
                print(f"Общее название звезды: {item['name']} \n Название созвездия: {item['constellation']} \n Можно ли увидеть звезду без телескопа: {item['is_visible']} \n Солнечный радиус звезды: {item['radius']}")
                found = True
                break
        if not found:
             print("Некорректный ввод")
    elif punkt == 3:
        flag = True
        name = input("Введите название звезды: ")
        constellation = input("Введите название созвездия: ")
        is_visible = input("Можно ли увидеть звезду без телескопа (да/нет): ")
        radius = input("Введите радиус звезды: ")
        try:
            radius = int(radius)
        except:
            flag = False
        if(not flag):
            print("Значение для радиуса введено неверно.")
        else:
            new = {
                'id': num,
                'name': name,
                'constellation': constellation,
                'is_visible': "да" if is_visible.lower() == 'да' else "нет", 
                'radius ': radius 
            }

            no_json.append(new) 
            with open("dump.json", 'w', encoding='utf-8') as file: 
                json.dump(no_json, file)
            print("Запись добавлена.")
        count += 1
        num+=1
        
    elif punkt == 4:
        count += 1
        record = input("Введите поле для удаления: ")
        found = False
        with open("dump.json", "w",   encoding = "utf-8") as file:
            for i, item in enumerate(no_json):
                if item["id"] == record:
                    del no_json[i]
                    print("Запись удалена")
                    found = True
                    break
            json.dump(no_json, file, indent = 4)
            if not found:
                print("Некорректный ввод")
    elif punkt == 5:
        print(f"{count} выполненных операций")
        break
    else:
        print("Нет такого пункта")