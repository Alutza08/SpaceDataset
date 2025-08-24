import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\Admin\PycharmProjects\ProjectEric\Space_Corrected.csv")
df = df.drop(columns=['Unnamed: 0', 'Unnamed: 0.1'])
df.columns = df.columns.str.strip()

###################### ГИПОТЕЗА 1 ##################
# #2. Перетворення дати у datetime
# df['Datum'] = pd.to_datetime(df['Datum'], errors='coerce')
#
# # 3. Витягуємо годину запуску
# df['Hour'] = df['Datum'].dt.hour
#
# # 4. Позначаємо, що таке "ранок" (наприклад, з 5 до 12)
# df['Morning'] = df['Hour'].between(5, 11)  # включно 5:00 - 11:59
#
# # 5. Визначимо приватні компанії (наприклад)
# private_companies = [
#     "SpaceX", "Blue Origin", "Rocket Lab", "Virgin Orbit", "Astra", "Orbital Sciences",
#     "Firefly", "OneSpace", "Relativity Space", "Interorbital Systems", "ExPace"
# ]
#
# # 6. Створюємо колонку з типом компанії
# df['Company Type'] = df['Company Name'].apply(lambda x: 'Private' if x in private_companies else 'Government')
#
# # 7. Створюємо колонку "Успішність"
# df['Success'] = df['Status Mission'].str.strip() == "Success"
#
# # 8. Фільтруємо тільки ранкові запуски
# morning_df = df[df['Morning'] == True]
#
# # 9. Рахуємо успішність для кожного типу компанії
# success_by_type = morning_df.groupby('Company Type')['Success'].mean() * 100
#
# print("Успішність запусків у ранкові години (%):")
# print(success_by_type)
#
# success_by_type.plot(kind='bar', color=['green', 'blue'])
# plt.ylabel('% Успішних запусків')
# plt.title('Успішність ранкових запусків: Приватні vs Державні компанії')
# plt.xticks(rotation=0)
# plt.ylim(0, 100)
# plt.show()
###################### ГИПОТЕЗА 1 ##################

###################### ГИПОТЕЗА 2 ##################
# Приводимо до нижнього регістру для зручності
# df['Status Mission'] = df['Status Mission'].str.strip().str.lower()
#
# # Функція для класифікації
# def classify_status(status):
#     if 'success' in status:
#         return 'Success'
#     else:
#         return 'Failure'
#
# # Нова колонка з класифікацією
# df['Mission Result'] = df['Status Mission'].apply(classify_status)
# df['Success'] = df['Mission Result'] == 'Success'
#
# df['Datum'] = pd.to_datetime(df['Datum'], errors='coerce')
# df['Year'] = df['Datum'].dt.year
#
# success_by_year = df.groupby('Year')['Success'].mean() * 100
#
# success_by_year.plot(marker='o', color='green', figsize=(12,6))
# plt.title("Успішність запусків по роках (усі варіанти success)")
# plt.xlabel("Рік")
# plt.ylabel("% Успішних запусків")
# plt.grid(True)
# plt.ylim(0, 100)
# plt.show()
###################### ГИПОТЕЗА 2 ##################

###################### ГИПОТЕЗА 3 ##################
# Очистка та нормалізація статусів місії
df['Status Mission'] = df['Status Mission'].str.strip().str.lower()

#Класифікація місії як Success / Failure
def classify_status(status):
   if 'success' in status:
       return 'Success'
   else:
       return 'Failure'

df['Mission Result'] = df['Status Mission'].apply(classify_status)
df['Success'] = df['Mission Result'] == 'Success'

# 🔹 Розрахунок успішності запусків по локаціях
success_by_location = df.groupby('Location')['Success'].mean() * 100

# 🔹 Топ-10 локацій за середньою успішністю
top_locations = success_by_location.sort_values(ascending=False).head(50)

# 🔹 Вивід
print("Успішність запусків за локацією (топ-20) (%):")
print(top_locations)

# 🔹 Побудова графіка
plt.figure(figsize=(12,6))
top_locations.plot(kind='barh', color='skyblue')
plt.xlabel('% Успішних запусків')
plt.title("Топ-20 локацій за успішністю запусків")
plt.xlim(0, 100)
plt.gca().invert_yaxis()
plt.grid(True, axis='x')
plt.tight_layout()
plt.show()
###################### ГИПОТЕЗА 3 ##################

###################### ГИПОТЕЗА 4 ##################
# df['Status Mission'] = df['Status Mission'].str.strip().str.lower()
#
# # Створюємо колонку Success (True, якщо в статусі є 'success')
# df['Success'] = df['Status Mission'].apply(lambda x: 'success' in x)
#
# # Групуємо по компаніях
# company_stats = df.groupby('Company Name')['Success'].agg(['mean', 'count']).sort_values(by='count', ascending=False)
# company_stats.rename(columns={'mean': 'Success Rate', 'count': 'Total Launches'}, inplace=True)
#
# # Вивід таблиці
# print("Успішність компаній залежно від кількості запусків:")
# print(company_stats)
#
# # Візуалізація
# plt.figure(figsize=(10, 6))
# sns.scatterplot(data=company_stats, x='Total Launches', y='Success Rate', size='Total Launches', hue='Success Rate', palette='coolwarm', legend=False)
# plt.title("Зв'язок між кількістю запусків і успішністю (по компаніях)")
# plt.xlabel('Кількість запусків')
# plt.ylabel('Успішність (%)')
# plt.ylim(0, 1.05)
# plt.grid(True)
# plt.tight_layout()
# plt.show()
###################### ГИПОТЕЗА 4 ##################

#print(df.info())
