# Moya — Cozy Hotel Management Game (GDD-Lite)

> A gentle, Animal Crossing–inspired hotel sim built in Godot. Soft goals, expressive décor, personality-driven guests, and a living diorama vibe.

---

## Design Pillars & Vibe
- **Gentle goals, no fail states** — mistakes become funny stories.
- **Expressive décor** — every item carries *tags* (color, style, vibe) that guests react to.
- **Small, living diorama** — cozy tilt camera, subtle DOF, tiny characters/big feelings.
- **Time & weather as ambience** — mood, not pressure.

---

## Core Game Loop (Short & Cozy)
1. **Morning Mail** — bookings, guest requests, deliveries.
2. **Arrange & Assign** — decorate rooms, place amenities, schedule staff.
3. **Hospitality Beats** — check-ins, room service mini-games, events.
4. **Evening Wind-Down** — stories with guests, stargazing, music.
5. **Reviews & Rewards** — unlock recipes, furniture, blueprints.

---

## Setting Hook
A petite **island rail-hotel** grows along a cliffside. New “wings” arrive by boat—modular, themed cars:
- **Forest Wing** · **Coral Wing** · **Observatory Wing** …

---

## Guests (Personality-Driven)
**Archetypes:** Bookish Moths · Surfing Capybaras · Traveling Bakers · Shy Ghosts (after midnight) · Retired Pirates

**Traits:** `Loves Pastels`, `Hates Clutter`, `Night Owl`, `Allergic to Ferns`, `Music Buff`

**Quirks → Mini-Quests:** find a lost postcard · serve tea at sunset · play a favorite record

### Relationship System
- **Memory Tokens** — fulfilling preferences grants keepsakes (e.g., Seashell, Pressed Leaf). Sets unlock vignettes/recipes.
- **Pen-Pal Letters** — arrive later with small gifts and new furniture patterns.

---

## Rooms & Décor (Tag System)
- Every item has tags: `["cozy","wood","green","retro","seaside","minimal"]`
- Each guest weighs desired tags; **room score** = sum of tag matches → **warmth rating** → **review**
- **Sets & Themes** — complete a 3-piece set for subtle glow/SFX (e.g., Forest set fireflies)

---

## Amenities & Mini-Games (Short, Tactile)
- **Tea Bar** — timing-based steep & pour
- **Vinyl Lounge** — match guest mood to records; tiny rhythm cue
- **Hot Springs** — leaf-skimming / temperature balancing
- **Laundry/Pressing** — fold silhouettes into outlines (satisfying snap)
- **Garden** — gentle planting; harvest dyes for décor fabrics

---

## Progression & Meta
- **Wing Unlocks** — gated by review milestones and cozy challenges (e.g., host 3 Night Owls)
- **Crafting Lite** — dye fabrics, embroider patterns, carve driftwood décor
- **Staff Friends** — e.g., sleepy bellhop pangolin; level via story beats, not grind

---

## Events & Seasons
- **Drizzle Festival (Autumn)** — warm light, rain SFX, limited recipes
- **Starlight Week (Winter)** — telescope nights; constellations → wallpaper patterns
- **Shell Swap (Summer)** — vendor trades rare pastel shells for DIYs
- **Bloom Parade (Spring)** — flower-themed décor combo requests

---

## Economy (Soft & Wholesome)
- **Coins** — stays & services
- **Keepsakes** — relationship currency
- **Vouchers** — event prizes  
Prices stay gentle; variety & expression over grind.

---

## Art Direction (ACNH-like Warmth in Godot)
**Style:** low-poly, hand-painted gradients, chunky silhouettes, minimal textures  
**Palette:** creamy pastels + one accent per room  
**Camera:** isometric-ish dollhouse; subtle vignette & shallow DOF

**Shaders**
- Matcap/toon ramp for soft shading
- Thin inverted-hull outline
- Foliage sway; sparkle for special décor

**Animation**
- Squash/overshoot on emotes
- Tiny footstep puffs
- Ambient loops (steam, fireflies)

---

## Godot Implementation Notes (Pragmatic)
- **3D / 2.5D** — `Node3D` rooms as modular scenes; fixed cozy camera
- **Navigation** — `NavigationServer3D` + per-floor navmeshes; doorways use off-mesh links
- **Tag System** — `DecorItem.tres` (`tags: Array[String]`, `comfort: int`)
- **Guest AI** — state machine: `Arriving → Exploring → Idle → Request → Sleeping`
- **Time & Weather** — global `WorldState` autoload; tween light/color; trigger SFX/particles
- **Save** — JSON/`ConfigFile` with versioned schema; room layout = item IDs + transforms
- **Signals** — `Guest.requested_service`, `Room.score_changed`, `Hotel.day_ended`
- **UI** — cozy cards; large touch targets; drag-drop décor with snap grid

---

## Signature Differentiators (Pick a Few)
1. **Spirits Night** — friendly ghosts check in after 10pm; reveal hidden décor tags  
2. **Soundscape Matching** — curate room sounds (rain, vinyl crackle, gulls) for comfort bonus  
3. **Scent Blends** — candles with notes (citrus/cedar) that map to tags & moods  
4. **Postcard Board** — guests leave art; players frame and display  
5. **Mini Dioramas** — zoom into shelf vignettes to place tiny collectibles  
6. **Rail-Car Wings** — rearrange whole wings like giant furniture for layout bonuses  
7. **Constellation Crafting** — trace stars to unlock wallpapers  
8. **Storybook Check-Ins** — each guest arrives with a 3-panel comic to complete by day’s end  
9. **Soft Cooking** — tea, toast, jam—forgiving breakfast loops  
10. **Night Market Pop-Ups** — rotating vendors with whimsical trade rules

---

## Scope & Schedules

### MVP (8–12 Weeks)
- **Space** — 1 floor, 4 rooms  
- **Content** — 20 décor items, 6 guests, 3 amenities (Tea Bar, Laundry, Garden)  
- **Systems** — day/night, rain toggle, mail, reviews, save/load  
- **Event** — 1 festival (Shell Swap)  
- **Staff** — 1 pal with 3 upgrade beats  
- **Polish** — footsteps, wind sway, soft DOF, gentle music loops

### Stretch Goals
- Photo mode + sticker overlays  
- Island expansion (dock, lighthouse spa)  
- Simple sharing (export/import room cards via QR)  
- Accessibility (dyslexic-friendly font, colorblind palettes, motion/DOF sliders)

---

## Starter Data Schemas (Suggestion)

```yaml
# DecorItem.tres (Resource)
id: string
name: string
comfort: int                 # contributes to warmth rating
tags: [string]               # e.g., ["cozy","wood","seaside"]
set_id: string | null        # for 3-piece set bonuses
mesh_path: string
icon_path: string
footprint: [int,int]         # grid width,height
place_rules:
  wall_mount: bool
  surface_only: bool
  outdoor_ok: bool
```

```yaml
# Guest.tres (Resource)
id: string
name: string
archetype: string            # e.g., "Bookish Moth"
traits: [string]             # e.g., ["Night Owl","Loves Pastels"]
tag_preferences:
  desired: { tag: weight }   # e.g., { "cozy": 2, "pastel": 1, "retro": 1 }
  disliked: { tag: weight }  # subtract from score
quirks: [string]             # quest hooks
favorite_items: [string]     # decor ids
schedule:
  wake: "09:00"
  nap: "15:00"
  sleep: "23:00"
rewards:
  tokens: [string]
  patterns: [string]
```

```yaml
# Review Scoring (pseudo)
room_score = Σ(item.tags ∩ guest.desired) - Σ(item.tags ∩ guest.disliked) + comfort_total/threshold
warmth_rating = clamp01(room_score / ideal_score)
review_tier = S/A/B/C by thresholds
```

---

## Scene Tree Blueprint (Example)

```
Hotel (Node3D)
├─ WorldState (Autoload / Singleton)
├─ Wings (Node3D)
│  ├─ ForestWing (Node3D)
│  └─ CoralWing  (Node3D)
├─ Rooms (Node3D)
│  ├─ Room_101 (Room: Node3D)
│  └─ Room_102 (Room)
├─ Guests (Node3D)
│  ├─ Guest_A (CharacterBody3D)
│  └─ Guest_B
├─ Amenities (Node3D)
│  ├─ TeaBar (Node3D)
│  ├─ Laundry (Node3D)
│  └─ Garden  (Node3D)
├─ Systems (Node)
│  ├─ Mailbox (Node)
│  ├─ ReviewSystem (Node)
│  └─ SaveLoad (Node)
└─ UI (CanvasLayer)
   ├─ MailPanel
   ├─ GuestCards
   ├─ DecorInventory
   └─ ReviewPopup
```

---

## Content Checklists (MVP Targets)

**Décor (20)**
- Beds (2), Rugs (2), Lamps (3), Plants (3), Shelves (2), Art (2), Tables (2), Chairs (2), Accent (2)

**Guests (6)**
- 2 day-active, 2 night-active (incl. 1 ghost), 2 flexible

**Mini-Games (3)**
- Tea Bar · Laundry · Garden

**Audio**
- 3 background records, 2 weather loops (rain, breeze), 6 foley snaps

---

## Versioning & Save Notes
- **Schema v0.1** — keep a `save_version` key; migrate forward via simple map
- **Room Layouts** — store `[{decor_id, transform, meta}]`
- **Daily Seed** — deterministic events/letters per day for cozy predictability

---

## Accessibility & Comfort
- Dyslexic-friendly font option
- Colorblind-safe palettes
- Sliders: motion, vignette, DOF strength
- Text size presets

---

**Status:** v0.1 (MVP-ready outline)  
**Working Title:** *Moya*
