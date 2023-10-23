import inquirer

def main():
    questions = [
        inquirer.List(
            'menu',
            message="What mode are you running your bot",
            choices=[
                "no-headless: show the current status of creating account",
                "headless: hide the current status of creating account"
                ],
        ),
    ]

    answers = inquirer.prompt(questions)
    selected_option = answers['menu']
    print(f"You selected: {selected_option}")

if __name__ == '__main__':
    main()