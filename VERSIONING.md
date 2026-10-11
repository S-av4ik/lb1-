# Політика версіонування

## Версії (SemVer)
Версія має вигляд **MAJOR.MINOR.PATCH**, наприклад `1.0.1`.

| Частина | Коли змінюється | Приклад |
|---------|-----------------|---------|
| MAJOR | зміна, яка ламає сумісність зі старою версією | 1.1.1 → 2.0.0 |
| MINOR | нова функція, стара працює як раніше | 1.0.0 → 1.1.0 |
| PATCH | виправлення помилки | 1.1.0 → 1.1.1 |

Теги у Git пишемо з літерою `v`: `v1.0.0`.

## Гілки (GitFlow)
- `main` — тільки стабільні релізи, на кожному релізі стоїть тег.
- `develop` — сюди зливаються готові фічі.
- `feature/*` — окрема гілка на кожну нову функцію, створюється від `develop`.
- `release/*` — підготовка релізу.
- `hotfix/*` — швидке виправлення помилки у `main`.

## Повідомлення комітів
Пишемо за схемою `тип(область): опис`:
- `feat` — нова функція (змінює MINOR);
- `fix` — виправлення помилки (змінює PATCH);
- `docs`, `test`, `chore` — документація, тести, дрібні зміни.

Приклад: `feat(auth): add login endpoint`.

## Команди Git
Нова фіча:
```bash
git checkout -b feature/add-login develop
git add .
git commit -m "feat(auth): add login endpoint"
git push origin feature/add-login
```
Після перевірки коду зливаємо у `develop`:
```bash
git checkout develop
git merge --no-ff feature/add-login
git push origin develop
```
Реліз:
```bash
git checkout main
git merge --no-ff develop
git tag -a v1.0.0 -m "Release 1.0.0"
git push origin main
git push origin v1.0.0
```

## Правила релізу
1. Усі фічі злиті у `develop`, тести проходять.
2. Оновлено `CHANGELOG.md` і release notes.
3. `develop` зливається у `main`, ставиться тег.
4. Історія релізів зберігається у `CHANGELOG.md` і в тегах Git.
