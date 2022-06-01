from classusers import User, Admin, Privilege

usuario = User('renato', 'martins')
usuario.describe_user()
usuario.greet_user()
usuario.increment_login_attempts(5)


admin = Admin('marley', 'martins')
admin.describe_user()
admin.privileges.show_privileges()
admin.greet_user()
admin.increment_login_attempts(7)