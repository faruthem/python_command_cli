# comun line interface
# Importamos el archivo json_manager
import json_manager
import click  # requiero click


@click.group()
def cli():
    pass


@cli.command()
@click.option('--name', required=True, help='Name of the user')
@click.option('--lastname', required=True, help='LastName of the user')
@click.pass_context
def new(ctx, name, lastname):  # ctx sirve para lanzar errores por consola
    if not name or not lastname:
        ctx.fail('the name and lastname are required')
    else:
        data = json_manager.read_json()
        new_id = len(data) + 1
        new_user = {
            'id': new_id,
            'name': name,
            'lastname': lastname
        }
        data.append(new_user)
        # print(data)
        json_manager.write_json(data)
        print(f"User {name} {lastname} created successfully with id {new_id}")


@cli.command()
def users():
    users = json_manager.read_json()
    for user in users:
        print(
            f"{user['id']} - {user['name']} - {user['lastname']}")


@cli.command()
@click.argument('id', type=int)
def user(id):
    data = json_manager.read_json()
    user = next((x for x in data if x['id'] == id), None)
    if user is None:
        print(f"User with id {id} not found")

    else:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")


@cli.command()
@click.argument('id', type=int)
@click.option('--name', help='Name of the user')
@click.option('--lastname', help='LastName of the user')
def update(id, name, lastname):
    data = json_manager.read_json()
    for user in data:
        if user['id'] == id:
            if name is not None:
                user['name'] = name
            if lastname is not None:
                user['lastname'] = lastname
            break
    json_manager.write_json(data)
    print(f"User with id {id} updated successfully")


@cli.command()
@click.argument('id', type=int)
def delete(id):
    data = json_manager.read_json()
    user = next((x for x in data if x['id'] == id), None)
    if user is None:
        print(f"User with id {id} not found")

    else:
        data.remove(user)
        json_manager.write_json(data)
        print(f"User with id {id} deleted successfully")


if __name__ == '__main__':
    cli()
