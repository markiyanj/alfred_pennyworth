Коли хижак полює, то з джунглів випадком чином береться тварина. 
Ця тварина може буде і самим хижаком. Для того, щоб це перевірити і розрізняти двух тварин з однаковою характеристикою 
використайте біліотеку [uuid](https://docs.python.org/3/library/uuid.html).
 Та при створені тварини присвоюйте її id унікальне значення.

Для роботи з випадковими числами можете скористатися бібліотекою [random](https://docs.python.org/3/library/random.html)

Якщо розбирати документацію бібліотек важко, то можете пошукати статті з прикладом використання.

Для того, щоб пройшли тести вам потрібно зробити класс Animal абстрактним та Jungle ітеруємим

Якщо не знаєте, як створити Джунглі та дивитися на процесс виживання, то ось приклад коду,
 який можна використати для дебагінгу 
 ```
if __name__ == "__main__":
    nature = animal_generator()

    jungle = Jungle()
    for i in range(10):
        animal = next(nature)
        jungle.add_animal(animal)

    while True:
        if not jungle.any_predator_left():
            break
        for animal in jungle:
            animal.eat(jungle=jungle)
        time.sleep(1)
```
`time.sleep` в прикладі для того, щоб убезпечети неуважних програмістів. 




