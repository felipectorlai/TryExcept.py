def main():
    employees = []

    while True:
        print("\nOpções:")
        print("1 - Inserir funcionário")
        print("2 - Listar funcionários")
        print("3 - Atualizar funcionário")
        print("4 - Deletar funcionário")
        print("0 - Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            list_employees(employees)
        elif choice == '3':
            update_employee(employees)
        elif choice == '4':
            delete_employee(employees)
        elif choice == '0':
            break
        else:
            print("Opção inválida. Escolha novamente.")

def add_employee(employees):
    try:
        code = input("Código do funcionário: ")
        name = input("Nome do funcionário: ")
        age = int(input("Idade do funcionário: "))
        salary = float(input("Salário do funcionário: "))

        employee = {
            'Código': code,
            'Nome': name,
            'Idade': age,
            'Salário': salary
        }

        employees.append(employee)
        print("Funcionário adicionado com sucesso.")
    except ValueError:
        print("Erro: Valor inválido para idade ou salário.")
    except Exception as e:
        print(f"Erro: {e}")

def list_employees(employees):
    if not employees:
        print("Nenhum funcionário cadastrado.")
    else:
        for idx, employee in enumerate(employees, start=1):
            print(f"\nFuncionário {idx}:")
            print(f"Código: {employee['Código']}")
            print(f"Nome: {employee['Nome']}")
            print(f"Idade: {employee['Idade']}")
            print(f"Salário: {employee['Salário']}")

def update_employee(employees):
    if not employees:
        print("Nenhum funcionário cadastrado.")
    else:
        code = input("Digite o código do funcionário a ser atualizado: ")
        found = False

        for employee in employees:
            if employee['Código'] == code:
                found = True
                print(f"Funcionário encontrado:\nNome: {employee['Nome']}")

                try:
                    age = int(input("Nova idade do funcionário: "))
                    salary = float(input("Novo salário do funcionário: "))

                    employee['Idade'] = age
                    employee['Salário'] = salary
                    print("Funcionário atualizado com sucesso.")
                except ValueError:
                    print("Erro: Valor inválido para idade ou salário.")
                except Exception as e:
                    print(f"Erro: {e}")

        if not found:
            print("Funcionário não encontrado.")

def delete_employee(employees):
    if not employees:
        print("Nenhum funcionário cadastrado.")
    else:
        code = input("Digite o código do funcionário a ser deletado: ")
        removed = False

        for employee in employees[:]:
            if employee['Código'] == code:
                employees.remove(employee)
                removed = True
                print("Funcionário removido com sucesso.")

        if not removed:
            print("Funcionário não encontrado.")

if __name__ == "__main__":
    main()
