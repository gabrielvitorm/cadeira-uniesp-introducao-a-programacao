import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="black")
        self.canvas.pack()
        self.snake = [(20, 20)]
        self.food = self.create_food()
        self.direction = "Right"
        self.score = 0
        self.draw_snake()
        self.draw_food()
        self.move_snake()
        self.master.bind("<KeyPress>", self.change_direction)

    def create_food(self):
        x = random.randint(0, 19) * 20
        y = random.randint(0, 19) * 20
        return (x, y)

    def draw_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            x1, y1 = segment
            x2, y2 = x1 + 20, y1 + 20
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="green", tag="snake")

    def draw_food(self):
        self.canvas.create_oval(self.food[0], self.food[1], self.food[0] + 20, self.food[1] + 20, fill="red", tag="food")

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            head_y -= 20
            if head_y < 0:
                head_y = 380
        elif self.direction == "Down":
            head_y += 20
            if head_y >= 400:
                head_y = 0
        elif self.direction == "Left":
            head_x -= 20
            if head_x < 0:
                head_x = 380
        elif self.direction == "Right":
            head_x += 20
            if head_x >= 400:
                head_x = 0
        new_head = (head_x, head_y)
        if new_head == self.food:
            self.score += 10
            self.food = self.create_food()
            self.snake.append(self.snake[-1])
            self.draw_food()
        else:
            self.snake.pop()
        self.snake.insert(0, new_head)
        self.draw_snake()
        self.master.after(100, self.move_snake)

    def change_direction(self, event):
        key = event.keysym
        if key in ["Up", "Down", "Left", "Right"]:
            if key == "Up" and self.direction != "Down":
                self.direction = "Up"
            elif key == "Down" and self.direction != "Up":
                self.direction = "Down"
            elif key == "Left" and self.direction != "Right":
                self.direction = "Left"
            elif key == "Right" and self.direction != "Left":
                self.direction = "Right"

root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
