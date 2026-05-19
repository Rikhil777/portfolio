# TODO

## Database fix for Railway (so portfolio data returns)
- [ ] Update `core/settings.py` to use `DATABASE_URL` when present (Railway), fallback to local SQLite.
- [ ] Ensure `railway` environment variables support this (DB_URL).
- [ ] Create/verify a local data export command path.
- [ ] Run a local export of current `db.sqlite3` contents into JSON fixtures.
- [ ] Load those fixtures on Railway DB.
- [ ] Confirm website pages render populated data.

