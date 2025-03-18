# Отчет по DI в функциональном стиле 1

Всё таки пошёл не по совсем правильному пути, и использовал
только функции для представления API. Однако в целом мне кажется,
что идея соотносится с тем, что требовалось, а именно
мы позволяем пользователю самому выбирать какую функцию
он хочет использовать для чтения команды.

```python
state = pr.RobotState(0, 0, 0.0, pr.WATER)
state = call_robot_function(pr.move, pr.transfer_to_cleaner, 10, state)
state = call_robot_function(pr.turn, pr.transfer_to_cleaner, 60.0, state)
state = call_robot_function(pr.set_state, pr.transfer_to_cleaner, pr.BRUSH, state)
state = call_robot_function(pr.move, pr.transfer_to_cleaner, 10, state)
```
