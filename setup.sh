#!/bin/bash

echo "🚀 Установка виртуального окружения..."
python3 -m venv venv
source venv/bin/activate

echo "📦 Установка зависимостей..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Установка завершена!"