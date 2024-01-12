def ex1(user_name, interval):
    data = []
    with open("ex1/log.txt", 'r') as file:
        lines = file.readlines()
        content = list(map(lambda x: x.strip().split(), lines))

        milisecondsInterval = sorted(interval)

        constraint = lambda x: x[2] == user_name and milisecondsInterval[1] > int(x[0]) > milisecondsInterval[0]
        data = list(filter(constraint, content))

        print(data)
