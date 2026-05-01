name: product-launch-prompts

description: Generate a complete suite of luxury product-launch creative prompts for any electronic gadget — a hero photography prompt, an exploded-parts photography prompt, a cinematic assembly video prompt, and a scroll-driven landing page build prompt — all derived from a single product name. Use this skill whenever the user wants prompts for product photography, exploded view renders, product reveal videos, product launch landing pages, or asks to "generate prompts for [a watch / drone / headphones / phone / camera / speaker / earbuds / controller / etc.]". Also trigger when the user mentions wanting Apple-keynote-style or Hodinkee-style product visuals, when they want to create a product reveal animation, or when they say things like "I want to make a launch page for X", "give me prompts to render X", or "I want to do for X what we did for the watch". Even if the user doesn't explicitly say the word "prompt", trigger this if they're asking for the assets needed to launch a luxury electronic product.

# Product Launch Prompts

Generate a coherent suite of four creative prompts — hero photo, exploded view, assembly video, and scroll-driven landing page — for any electronic gadget, all anchored to a single luxury minimalist brand identity.

## How This Skill Works

The skill takes a product (e.g., "watch", "over-ear headphones", "drone", "wireless earbuds", "gaming controller") and produces a filled-in template with all four prompts ready to paste into image, video, and code-generation tools.

The trick is that all four prompts share an identical visual identity — same materials, same accent color, same signature detail — so the resulting hero photo, exploded view, video, and landing page feel like they're for the same product from the same brand. The 11 variables defined below are what hold that coherence together.

## The Workflow

1. **Identify the product.** Get the product name from the user. If it's vague (just "headphones"), pick the most photogenic variant (over-ear > earbuds for drama). Don't ask the user to choose — make the call and mention it briefly.
2. **Fill in the 11 variables** using the selection guidance below. Make tasteful, opinionated choices — don't ask the user to pick for you. Apply the rules under "Cross-Variable Coherence Rules" before locking in.
3. **Substitute the variables into the 4 prompt templates** below, verbatim. Do not paraphrase the templates.
4. **Output as a single markdown file** named `<product-slug>-launch-prompts.md` in `/mnt/user-data/outputs/`, then present it with `present_files`. The file should contain: the filled variables table, the 4 prompts each in its own copyable code block, and a short "how to use" closer.

## The 11 Variables

| Variable | What it captures |
|---|---|
| `{PRODUCT_TYPE}` | Generic product noun ("over-ear headphones", "compact mirrorless camera") |
| `{FORM_FACTOR}` | Shape, size, profile in 1 sentence |
| `{PRIMARY_MATERIAL}` | Hero material + finish (the chassis) |
| `{SECONDARY_MATERIAL}` | Soft / contact material (strap, pads, grip) |
| `{SURFACE_DETAIL}` | The texture story on the main visible surface |


| `{ACCENT_COLOR}` | The single pop color, used sparingly |
| `{SIGNATURE_DETAIL}` | The one visual element that makes this product distinctive |
| `{KEY_COMPONENTS}` | 5-8 parts shown in the exploded view, ordered top to bottom |
| `{FUNCTIONAL_ELEMENT}` | A working mechanical/functional part visible up close |
| `{BRAND_REFERENCE_AESTHETIC}` | The brand mood reference (e.g., "Hodinkee", "Bang & Olufsen") |
| `{HERO_ANGLE}` | Beauty-shot camera angle for the final shot |

## Selection Guidance

These are the calls that make or break the result. Make confident, opinionated choices — never ask the user "what color should the accent be?" Pick it.


### {PRIMARY_MATERIAL} — pick from the luxury palette

Brushed titanium, anodized aluminum, machined steel, ceramic, magnesium alloy, polished tungsten, machined brass. Avoid plastic — even if the real product is plastic, render it in metal. We're going for luxury.

### {SECONDARY_MATERIAL} — earthy, tactile, warm

Vegetable-tanned leather (cognac/espresso/saddle), Alcantara, woven Cordura, vulcanized rubber, Italian wool felt, sailcloth, FKM rubber, knit textile. Should warm-contrast against the cool primary material.

### {ACCENT_COLOR} — bold but not loud, used sparingly

Brushed orange, burnt copper, electric teal, oxblood red, mustard yellow, signal green, deep ultramarine, blood orange. Pick ONE, never two. Apply it to a single small element.

### {SIGNATURE_DETAIL} — the "this is the one" element

This is the hardest variable to get right and the most important. It should be:
- Visible in close-up
- Functional, not decorative (an exposed mechanism, a colored hand, a glowing element)
- Strongly associated with the {ACCENT_COLOR}

Examples: orange minute hand (watch), exposed copper voice coil (headphones), glowing power ring (speaker), brushed-orange shutter button (camera), illuminated D-pad ring (controller), signal-green LED gimbal ring (drone).

### {KEY_COMPONENTS} — the anatomy

- Must reflect the actual physical structure of the product type — not invented parts
- 5-8 components — fewer feels empty, more feels noisy
- Order top-to-bottom in roughly the order you'd disassemble them
- Briefly name the material/finish for each so the exploded view stays coherent

### {BRAND_REFERENCE_AESTHETIC} — match the product category


## Output File Format

Save the final document as `<product-slug>-launch-prompts.md` (e.g., `drone-launch-prompts.md`, `over-ear-headphones-launch-prompts.md`) in `/mnt/user-data/outputs/`. Use this exact structure:

```
# {Product Title} Launch Prompt Suite

A complete creative-asset suite for launching the {Product Type}, anchored to a single luxury minimalist identity.

## Brand Identity

| Variable | Value |
|---|---|
| Product Type | ... |
| Form Factor | ... |
| Primary Material | ... |
| Secondary Material | ... |
| Surface Detail | ... |
| Accent Color | ... |
| Signature Detail | ... |
| Key Components | ... |
| Functional Element | ... |
| Brand Reference Aesthetic | ... |
| Hero Angle | ... |

## 1. Hero Product Shot
> Use in: Midjourney, Flux, Nano Banana, Imagen
[Template 1 with substitutions in a code block]

## 2. Exploded Parts Shot
> Use in: same image generator as above
[Template 2 with substitutions in a code block]

## 3. Assembly Video
> Use in: Runway, Kling, Veo, Sora — generate 5-10s at 24fps
[Template 3 with substitutions in a code block]

## 4. Scroll-Driven Landing Page
> Use in: Claude Code, Cursor, or any Claude artifact — drop in a folder of rendered PNG frames first
[Template 4 with substitutions in a code block]

## How to Use This Suite
1. Run prompt 1 for the hero shot
2. Run prompt 2 for the exploded view
3. Run prompt 3 to generate the assembly video
4. Extract the rendered video into ~120 PNG frames (use ffmpeg or a frame-extractor), drop them in a folder, and feed prompt 4 + the folder to Claude Code or Cursor to build the landing page
```

After creating the file, present it with `present_files` and give a one-line summary that names the product and the chosen accent color / signature detail (so the user can see the creative call you made at a glance).

## A Worked Example

If the user says "drone", produce a variable set like this — confident, opinionated, coherent:

| Variable | Value |
|---|---|
| `{PRODUCT_TYPE}` | quadcopter drone |
| `{FORM_FACTOR}` | compact 220mm wheelbase, foldable arms, 35mm-thick fuselage |
| `{PRIMARY_MATERIAL}` | matte machined magnesium alloy in graphite gray |
| `{SECONDARY_MATERIAL}` | textured rubberized propeller mounts and grip pads |
| `{SURFACE_DETAIL}` | subtle linear brushed grain across the top fuselage |
| `{ACCENT_COLOR}` | signal green |
| `{SIGNATURE_DETAIL}` | thin signal-green LED ring around the front camera gimbal |
| `{KEY_COMPONENTS}` | top fuselage shell, internal flight controller PCB, battery cell, motor stack with carbon-fiber propellers, gimbal-mounted camera, landing skids, bottom shell |
| `{FUNCTIONAL_ELEMENT}` | flush-mounted gimbal camera and recessed power button |
| `{BRAND_REFERENCE_AESTHETIC}` | DJI Mavic luxury edition / Skydio |
| `{HERO_ANGLE}` | three-quarter front view from slightly above, one arm closest to camera |

That set passes the coherence rules: signal green appears in the LED ring (signature) and on the components, the rubberized grips show in the hero angle, brand reference matches the drone category. Substitute and you're done.

## Style Defaults

Unless the user explicitly asks for a different mood:
- Aesthetic is always **ultra-premium luxury minimalist**
- Background is always **deep matte black** for hero, exploded, and video
- Lighting is always **studio rim light from upper left**
- Voice is always **product as quiet object** — no logos, no text in the renders themselves

If the user wants a different aesthetic ("make it playful retro", "outdoor / sporty", "futuristic neon"), override the brand reference, materials, and accent color accordingly, but keep the four-prompt structure intact.

`## Brand Identity`

`| Variable | Value |`

`|---|---|`

`| Product Type | ... |`

`| Form Factor | ... |`

`| Primary Material | ... |`

`| Secondary Material | ... |`

`| Surface Detail | ... |`

`| Accent Color | ... |`

`| Signature Detail | ... |`

`| Key Components | ... |`

`| Functional Element | ... |`

`| Brand Reference Aesthetic | ... |`

`| Hero Angle | ... |`

`## 1. Hero Product Shot`

`> Use in: Midjourney, Flux, Nano Banana, Imagen`

`[Template 1 with substitutions in a code block]`

`## 2. Exploded Parts Shot`

`> Use in: same image generator as above`

`[Template 2 with substitutions in a code block]`

`## 3. Assembly Video`

`> Use in: Runway, Kling, Veo, Sora — generate 5-10s at 24fps`

`[Template 3 with substitutions in a code block]`

`## 4. Scroll-Driven Landing Page`

`> Use in: Claude Code, Cursor, or any Claude artifact — drop in a folder of rendered PNG frames first`

`[Template 4 with substitutions in a code block]`

`## How to Use This Suite`

`1. Run prompt 1 for the hero shot`

`2. Run prompt 2 for the exploded view`

`3. Run prompt 3 to generate the assembly video`

`4. Extract the rendered video into ~120 PNG frames (use ffmpeg or a frame-extractor), drop them in a folder, and feed prompt 4 + the folder to Claude Code or Cursor to build the landing page`

`````

`After creating the file, present it with `present_files` and give a one-line summary that names the product and the chosen accent color / signature detail (so the user can see the creative call you made at a glance).`
`## A Worked Example`

`If the user says "drone", produce a variable set like this — confident, opinionated, coherent:`

`| Variable | Value |`

`|---|---|`

`| `{PRODUCT_TYPE}` | quadcopter drone |`

`| `{FORM_FACTOR}` | compact 220mm wheelbase, foldable arms, 35mm-thick fuselage |`

`| `{PRIMARY_MATERIAL}` | matte machined magnesium alloy in graphite gray |`

`| `{SECONDARY_MATERIAL}` | textured rubberized propeller mounts and grip pads |`

`| `{SURFACE_DETAIL}` | subtle linear brushed grain across the top fuselage |`

`| `{ACCENT_COLOR}` | signal green |`

`| `{SIGNATURE_DETAIL}` | thin signal-green LED ring around the front camera gimbal |`

`| `{KEY_COMPONENTS}` | top fuselage shell, internal flight controller PCB, battery cell, motor stack with carbon-fiber propellers, gimbal-mounted camera, landing skids, bottom shell |`

`| `{FUNCTIONAL_ELEMENT}` | flush-mounted gimbal camera and recessed power button |`

`| `{BRAND_REFERENCE_AESTHETIC}` | DJI Mavic luxury edition / Skydio |`

`| `{HERO_ANGLE}` | three-quarter front view from slightly above, one arm closest to camera |`

`That set passes the coherence rules: signal green appears in the LED ring (signature) and on the components, the rubberized grips show in the hero angle, brand reference matches the drone category. Substitute and you're done.`

`## Style Defaults`

`Unless the user explicitly asks for a different mood:`

- `Aesthetic is always **ultra-premium luxury minimalist**`
- `Background is always **deep matte black** for hero, exploded, and video`
- `Lighting is always **studio rim light from upper left**`
- `Voice is always **product as quiet object** — no logos, no text in the renders themselves`

`If the user wants a different aesthetic ("make it playful retro", "outdoor / sporty", "futuristic neon"), override the brand reference, materials, and accent color accordingly, but keep the four-prompt structure intact.`