import datetime
import pytest
import datetime

@pytest.fixture()
def timing():
    start = datetime.datetime.now()
    start = start.time()
    print(f'Начало выполнения метода {start}')
    yield
    end = datetime.datetime.now()
    end = end.time()
    print((f'Окончание выполнения метода {end}'))


@pytest.fixture(autouse=True)
def time():
    start = datetime.datetime.now()
    yield
    end = datetime.datetime.now()
    time = end - start
    print(f'Время выполнения метода {time}')