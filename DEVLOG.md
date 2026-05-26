# DIVA — Dev Log

## Project
2D platformer built with Python + pygame.
Repo: https://github.com/firstflye/diva

---

## Status Legend
- [ ] Not started
- [~] In progress
- [x] Done

---

## PHASE 1 — Core Loop
- [x] Folder structure created
- [x] main.py — entry point
- [x] settings.py — constants (⚠️ BASE_DIR bug, needs fix)
- [x] src/game.py — game loop skeleton (⚠️ no state loaded yet)
- [ ] Fix BASE_DIR in settings.py
- [ ] src/states/base_state.py
- [ ] src/states/menu.py
- [ ] Wire menu state into game.py

## PHASE 2 — Player & World
- [ ] src/entities/base_entity.py
- [ ] src/entities/player.py
- [ ] src/systems/input_handler.py
- [ ] src/systems/physics.py
- [ ] src/world/tilemap.py
- [ ] levels/level_01.json (basic tile grid)
- [ ] src/world/level.py
- [ ] src/states/playing.py

## PHASE 3 — Polish
- [ ] src/world/camera.py
- [ ] src/ui/hud.py
- [ ] src/states/paused.py
- [ ] src/states/game_over.py
- [ ] src/entities/enemy.py
- [ ] src/ui/button.py
- [ ] src/systems/animation.py
- [ ] src/entities/projectile.py

## PHASE 4 — Content & Audio
- [ ] levels/level_02.json
- [ ] Asset loading (images, sounds)
- [ ] Background music
- [ ] SFX (jump, land, hit)
- [ ] Save/load system (saves/save_01.json)

---

## Known Bugs / Issues
- BASE_DIR in settings.py goes up one directory too many
- game.py has unused imports (os, random, math, listdir)
- No state is loaded on startup — window opens black

## Notes
- Always implement dependency files before files that import them
- Use dt (delta time) for all movement
- Keep magic numbers in settings.py only
