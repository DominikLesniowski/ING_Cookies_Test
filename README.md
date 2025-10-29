# Instrukcja uruchomienia testu

## 1.Sklonuj repozytorium

### W terminalu wykonaj polecenie:
```
git clone https://github.com/DominikLesniowski/ING_Cookies_Test.git
```
### Przejdź do katalogu projektu:
```
cd ING_Cookies_Test
```
## 2.Utwórz i aktywuj wirtualne środowisko

### W katalogu z projektem stwórz venv:
```
python3 -m venv venv 
```
### Aktywuj środowisko:
 
- Na macOS/Linux:
```
source venv/bin/activate  
```
- Na Windows:
```
venv\Scripts\activate
```

## 3.Zainstaluj potrzebne pakiety

```
pip install -r requirements.txt
```

## 4.Zainstaluj przeglądarki Playwright
```
playwright install
```

## 5.Uruchom test

```
pytest tests/test_cookies.py
```