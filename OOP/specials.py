mylist = [1, 2, 3]
# myString = "This is my stringth"

# print(len(mylist))
# print(len(myString))


class Movie:
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie object has been created")

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print("Movie has been deleted")


m = Movie("Film name", "Director name", 123)

# print(str(mylist))
print(str(m))

# print("a0")
# m.__str__()
# print("a1")

# print(type(m))
# print(len(m))

# del m

# print(m)
