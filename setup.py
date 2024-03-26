import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Pong",
    options={"build_exe": {"packages":["pygame"],"include_files":["Ball.png", "Paddle.png"]}},
    executables = executables
)