import datetime

task_name = 'Nauka Pythona'
expected_time = int(input('Czas pracy: '))
priority = int(input('Priorytet zadania: '))
frame = '=' * 20

is_urgent = priority >= 2


print('=' * 3, 'Menedżer zadań', '=' * 3)
print('KARTA ZADANIA:', task_name)
print('Czas:', expected_time // 60, 'godz', expected_time % 60, 'min')
print('Priorytet:', priority,end=' | ')
print('Pilne:', is_urgent)
print(frame)