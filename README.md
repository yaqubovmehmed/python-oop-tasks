# Python OOP Practice Tasks

A set of small exercises from a Python backend course, focused on classes, inheritance, constructors, and calling parent methods with `super()`.

## Exercises in `oop-task.py`

1. **Devices** — a shared `Texnika` parent class with notebook, television, and smartphone subclasses.
2. **Transport** — a `Transport` parent class with electric car, supercar, and truck subclasses.
3. **University** — university staff and student roles, followed by computer and furniture inventory objects.

Class and attribute names in the source are kept as written in the original Uzbek-language exercises. The project uses only the Python standard library.

## Run

```bash
python oop-task.py
```

The file defines the classes but does not instantiate them, so running it produces no output. To explore the classes, create instances in a Python shell or add an example under a `__main__` block.

## Learning goals

- Reuse common fields through inheritance
- Initialize parent classes with `super().__init__(...)`
- Add fields and display methods in subclasses
- Model related objects with simple class hierarchies

This is a learning exercise, not a production-ready inventory system.
