🇬🇧 [English](README.md) | 🇷🇺 **Русский**

[![Версия](https://img.shields.io/github/v/release/teknokomo/hermes-max-connector?label=version&color=blue&sort=semver)](https://github.com/teknokomo/hermes-max-connector/releases/latest)
[![Лицензия: Омская Открытая Лицензия](https://img.shields.io/badge/license-Omsk%20Open%20License-green)](LICENSE-RU.md)

![Технокомо — 73-й Меридиан](docs/assets/teknokomo-om73-ru.jpg)

# Важно! Grave! Important!

- Пролетарии всех стран, соединяйтесь!
- Workers of the world, unite!
- Proletoj el ĉiuj landoj, unuiĝu!

# Hermes MAX Connector

**Внимание: версия 0.1.0 — первый публичный выпуск. Перед включением коннектора проверьте настройки безопасности и транспорта.**

## Разработчики

Разработано [Текнокомо](https://universo.pro/).<br>
Сделано при поддержке [Консорциума «73-й Меридиан»](https://om73.ru).

## Обзор

Hermes MAX Connector добавляет MAX в Hermes Agent как адаптер платформы. Он получает сообщения MAX через производственный webhook или включаемый только для разработки long polling, применяет политику профиля и отправляет ответы через MAX Bot API.

Публичный пакет называется hermes-max-connector. Зарегистрированная платформа Hermes и ключ конфигурации остаются max, поэтому настройки по-прежнему находятся в platforms.max.

## Возможности

- Для личных сообщений используются pairing Hermes и настроенный список разрешённых пользователей.
- Группы по умолчанию отключены; для них нужно явно включить функцию и разрешить ID чата. Для нативных действий права группы проверяются повторно.
- Webhook требует настроенный общий секрет; повторы отсеиваются в памяти, а при необходимости — с сохранением состояния в SQLite профиля.
- Входящие вложения загружаются только с разрешённых медиа-хостов MAX и кешируются в целевом профиле Hermes.
- Исходящие файлы ограничены заданными корнями media_roots и проверяются по типу и размеру.
- Сообщения длиннее 4 000 символов разбиваются на части без потери текста.

## Установка

Установите файлы проекта в каталог `plugins` внутри Hermes home активного профиля. Для профиля default без пользовательского HERMES_HOME это ~/.hermes; для именованного профиля это `<Hermes root>/profiles/<name>`. Перед копированием задайте HERMES_PROFILE_HOME этому каталогу; для именованного профиля не оставляйте значение по умолчанию:

```bash
# For a named profile, set this to that profile's Hermes home.
HERMES_PROFILE_HOME="${HERMES_HOME:-$HOME/.hermes}"
mkdir -p "$HERMES_PROFILE_HOME/plugins/hermes-max-connector"
cp adapter.py __init__.py plugin.yaml "$HERMES_PROFILE_HOME/plugins/hermes-max-connector/"
```

После публикации Hermes также сможет установить плагин из публичного репозитория; для установки и включения выберите один и тот же профиль.

Установите aiohttp в среду Python, которую использует Hermes. Настройте MAX_BOT_TOKEN и доверенный CA bundle, затем включите hermes-max-connector командой hermes plugins enable hermes-max-connector. Для именованного профиля используйте `hermes -p <name> plugins enable hermes-max-connector`. В config.yaml используйте ключ платформы max.

## Настройка

| Параметр | Обязателен | Назначение и значение по умолчанию |
|---|---|---|
| MAX_BOT_TOKEN | Да | Учётные данные MAX Bot API; обязательны. |
| MAX_ALLOWED_USERS | Нет | Список ID пользователей MAX через запятую для личных сообщений; по умолчанию пуст. |
| MAX_ALLOW_ALL_USERS | Нет | Разрешает любого отправителя личного сообщения при значении true; по умолчанию false. |
| MAX_POLLING_DEV | Нет | Включает long polling для разработки при значении true; по умолчанию false. |
| MAX_POLL_TIMEOUT | Нет | Время ожидания long polling в секундах; по умолчанию 30, допустимый диапазон 1–90. |
| MAX_CA_BUNDLE | Нет | Профильный PEM CA bundle для проверяемого TLS MAX API; нужен для API-соединения, если путь не задан через platforms.max.ca_bundle. |
| MAX_HOME_CHANNEL | Нет | Получатель MAX для cron-доставки Hermes; по умолчанию не задан. |
| MAX_WEBHOOK_SECRET | Условно | Общий секрет для проверки X-Max-Bot-Api-Secret при включённом webhook. |

Несекретные параметры задаются в platforms.max. Адаптер также поддерживает allowed_users, allow_all_users, webhook, webhook_host, webhook_port, webhook_path, media_roots, persistent_state, markdown и настройки групп. Пример только с placeholders находится в config/example.yaml.

Для личных сообщений используется pairing Hermes. MAX_ALLOWED_USERS добавляет статический список разрешённых пользователей; по умолчанию доступ не открыт всем. Групповые диалоги отключены. Чтобы включить группу, задайте groups.enabled и укажите ID чата в groups.allowed_chats. Оставьте require_mention включённым, если нет явной причины принимать сообщения без обращения. Пассивный сбор неадресованных сообщений и документов по умолчанию отключён; установите groups.observe_unmentioned_group_messages: true только если вы явно хотите сохранять их в истории сессии. MAX_ALLOW_ALL_USERS используйте только в контролируемой среде разработки.

## Транспорт

Webhook — производственный транспорт. Установите platforms.max.webhook: true, задайте MAX_WEBHOOK_SECRET и направьте loopback listener через доверенный HTTPS reverse proxy на порту 443. Адаптер не создаёт подписку MAX: настройте её через MAX Bot API и включите типы message_created, message_callback, message_edited и message_removed. Укажите в поле `secret` подписки то же значение, что и в `MAX_WEBHOOK_SECRET` (5–256 букв, цифр, дефисов или подчёркиваний, как требует MAX); MAX передаёт его в заголовке `X-Max-Bot-Api-Secret` только при настроенном секрете, а коннектор отклоняет запросы без заголовка или с несовпадающим значением.

При создании и обслуживании подписки следуйте [требованиям MAX к webhook](https://dev.max.ru/docs-api/methods/POST/subscriptions).

Коннектор возвращает HTTP 200 после завершения обработчика обновления. При ошибке обработчика, повторной доставке во время обработки или тайм-ауте возвращается HTTP 503, чтобы MAX мог повторить запрос. Обработка ограничена 25 секундами в пределах 30-секундного окна ответа.

Long polling предназначен только для разработки и по умолчанию отключён. Для контролируемого тестового бота задайте MAX_POLLING_DEV=true. Одновременно включить webhook и polling нельзя.

## TLS и вложения

Запросы к MAX API требуют проверки сертификата и имени хоста с помощью доверенного профильного CA bundle. Задайте MAX_CA_BUNDLE или platforms.max.ca_bundle. Коннектор не отключает проверку TLS. Не используйте verify=False и не добавляйте посторонний корневой сертификат в системное хранилище.

Входящие медиа загружаются с разрешённых CDN-хостов MAX с ограничением 20 МиБ и кешируются для целевого профиля Hermes. Для исходящих медиа требуется media_roots; размер изображений ограничен 50 МиБ, а других файлов — 50 МиБ. Файлы вне этих каталогов отклоняются. Принимаются только поддерживаемые типы медиа и хосты загрузки MAX.

Необязательная интеграция с document-store — компонент `document-store` проекта [hermes-document-platform](https://github.com/teknokomo/hermes-document-platform), публикуемый как плагин `omisa-document-store`, — обеспечивает профильное автосохранение документов, если он установлен. Без него MAX Connector всё равно регистрируется и обрабатывает обычный платформенный трафик; недоступно только автосохранение документов. Автосохранение работает только в групповых чатах. Документы из личных сообщений попадают в кэш, но не сохраняются в постоянное хранилище.

## Состояние и ограничения

При включённом persistent_state состояние дедупликации webhook и интерактивных токенов хранится в SQLite профиля max/reliability.db. В памяти сохраняются до 4 096 последних идентификаторов webhook. Срок хранения записей SQLite — 7 дней. Максимальный размер webhook тела — 1 МиБ.

Длина исходящего сообщения MAX ограничена 4 000 символами; длинный текст разбивается автоматически. Уведомления о наборе текста работают по возможности. Long polling предназначен для разработки; поведение MAX API может зависеть от прав бота и поддерживаемых типов событий.

## Проверка

Из репозитория или распакованного исходного дистрибутива установите зафиксированную среду разработки и выполните автономные проверки:

```bash
uv sync --locked --group dev
uv run pytest -q
uv run python -m compileall -q adapter.py __init__.py conftest.py tests.py tests tools
uv run ruff check adapter.py __init__.py conftest.py tests.py tests tools
uv run bandit -r adapter.py __init__.py -c pyproject.toml
uv run python tools/check_readme_parity.py
uv run python tools/check_release_hygiene.py --filesystem
sha256sum -c MANIFEST.sha256
uv run python -m build
uv run twine check dist/*
```

Тесты используют фиктивные секреты и подменённые запросы MAX API; HTTP-приём проверяется временным loopback listener. Матрица модульных тестов Python 3.11–3.14 предоставляет минимальную границу Hermes. Отдельные задания CI проверяют холодную загрузку плагина на официальных Hermes v0.22.4 и v0.22.5 с требуемой им средой Python; без HERMES_SOURCE_DIR этот интеграционный тест явно пропускается. Точные upstream commit и команды совместимости приведены в .github/workflows/ci.yml.

Перед commit добавьте нужные файлы в индекс и выполните `uv run python tools/check_release_hygiene.py` для проверки фактического Git index. Проверка файловой системы читает текущие исходники; обе проверки дополняют ручной просмотр имён, идентификаторов и закрытого контекста.

## Безопасность и файлы проекта

Прочитайте [SECURITY.md](SECURITY.md) о границах доверия и сообщении об уязвимостях, [CHANGELOG.md](CHANGELOG.md) об истории релизов и [LICENSE-RU.md](LICENSE-RU.md) о лицензии. Инструкция по webhook находится в [deploy/README.md](deploy/README.md).
