import random
import whoisgame.models as wm


def randomize_game(difficulty_number):
    employee_block = []
    answer_list = []
    photo = random.choice(wm.Photograph.objects.all())
    for i in range(1, photo.employee_number + 1, 1):
        employees = []
        order = wm.Order.objects.filter(photo=photo).get(order=i)
        order.employee.spawn_counter += 1
        order.employee.save()
        employees.append(order.employee)
        answer_list.append(
            {
                "id": order.employee.id,
                "first_name": order.employee.first_name,
            }
        )
        for employee in random.choices(
            wm.Employee.objects.filter(
                gender=order.employee.gender
            ).exclude(
                first_name=order.employee.first_name
            ),
            k=1,
        ):
            employees.append(employee)

        random.shuffle(employees)
        employee_block.append(employees)

    return photo, employee_block, answer_list


def count_spawn_occurence(employees):
    for employee in employees:
        pass