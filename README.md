1. Create Virtual Environment

```
python -m venv data-warehouse
```

2. Run Virtual Environment

```
data-warehouse/Scripts/activate # windows
source data-warehouse/bin/activate # macos/linux
```

3. Install Python & Javascript libraries

```
pip install -r requirements.txt
```

4. Copy .env.example contents to a new .env file (you can customize your MySQL database URI)

```
cp .env.example .env
```

4. Run python app

```
python app.py
```
