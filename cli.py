import json_manager
import click


@click.group()
def cli():
    pass


@cli.command()
# Opciones de los comandos
@click.option('--name', required=True, help='Name of the user')
@click.option('--lastname', required=True, help='Lastname of the user')
# Para enviar el contexto
@click.pass_context
def new(ctx, name, lastname):
    if not name or not lastname:
        ctx.fail("The name and lastname are required")
    else:
        data = json_manager.read_json()

        new_id = len(data) + 1
        new_user = {
            'id': new_id,
            'name': name,
            'lastname': lastname,
        }
        data.append(new_user)

        json_manager.write_json(data=data)
        print(f"User {name} {lastname} created successfully with id {new_id}")


@cli.command()
def users():
    users = json_manager.read_json()

    for user in users:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")


@cli.command
# Argument es el valor que tu le envías al comando
@click.argument('id', type=int)
def user(id):
    users = json_manager.read_json()
    user = next((x for x in users if x['id'] == id), None)
    if user is None:
        print(f"User with id {id} not found")
    else:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")


@cli.command
@click.argument('id', type=int)
def delete(id):
    users = json_manager.read_json()
    user = next((x for x in users if x['id'] == id), None)
    if user is None:
        print(f"User with id {id} not found")
    else:
        users.remove(user)
        json_manager.write_json(users)
        print(f"User with id {id} deleted successfully")


@cli.command
@click.argument('id', type=int)
@click.option('--name', required=False, help='Name of the user')
@click.option('--lastname', required=False, help='Lastname of the user')
def update(id, name, lastname):
    users = json_manager.read_json()
    for user in users:
        if user['id'] == id:
            if name is not None:
                user['name'] = name
            if lastname is not None:
                user['lastname'] = lastname
            break

    json_manager.write_json(users)
    print(f"User with id {id} updated successfully")


if __name__ == '__main__':
    cli()
