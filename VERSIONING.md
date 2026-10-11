# Політика версіонування

## Семантичне версіонування (SemVer) — MAJOR.MINOR.PATCH
| Частина | Коли змінюється | Приклад |
|---------|-----------------|---------|
| MAJOR | зламна зміна, несумісність API | 1.1.1 → 2.0.0 |
| MINOR | нова функціональність, сумісна зі старою | 1.0.0 → 1.1.0 |
| PATCH | виправлення помилок без зміни API | 1.1.0 → 1.1.1 |

Прапорці пре-релізів: `1.1.0-rc.1`. Теги мають формат `vMAJOR.MINOR.PATCH`.

## Git-стратегія: GitFlow (спрощений)
- `main` — лише стабільні релізи, кожен коміт має тег.
- `develop` — інтеграція готових фіч.
- `feature/*` — одна гілка на фічу, створюється від `develop`.
- `release/*` — підготовка релізу (за потреби; у команді 1–2 осіб можна пропустити).
- `hotfix/*` — термінові виправлення від `main`, зливаються в `main` і `develop`.

```
main     ●─────────────────────●── v1.0.0 ──────────● v1.0.1
          \                   /                     ^
develop    ●───●─────────●───●──────────────────────/ (hotfix)
                \       /
feature/*        ●───●─┘
```

## Формат комітів (Conventional Commits)
`feat(scope): ...` → MINOR; `fix(scope): ...` → PATCH; `feat!:` або `BREAKING CHANGE:` → MAJOR; також `docs`, `test`, `chore`, `ci`.

## Приклад команд
```bash
git checkout -b feature/add-login develop
git add .
git commit -m "feat(auth): add login endpoint"
git push origin feature/add-login
# після code review
git checkout develop
git merge --no-ff feature/add-login
git push origin develop
# реліз
git checkout main
git merge --no-ff develop
git tag -a v1.0.0 -m "Release 1.0.0"
git push origin main v1.0.0
```

## Правила релізу
1. Усі фічі злиті в `develop`, тести проходять.
2. Оновлено `CHANGELOG.md` і release notes (за `RELEASE_TEMPLATE.md`).
3. `develop` зливається в `main` з `--no-ff`, ставиться тег.
4. Історія релізів ведеться у `CHANGELOG.md` та в тегах Git.
