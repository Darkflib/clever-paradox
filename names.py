#!/usr/bin/env python3
import random

ADJECTIVES = [
    "Agile", "Amber", "Ancient", "Arcane", "Arctic", "Ashen", "Astral", "Balanced", "Bitter",
    "Black", "Blazing", "Bleak", "Blind", "Bold", "Bright", "Brisk", "Broken", "Bronze", "Burning",
    "Calm", "Candid", "Celestial", "Cerulean", "Charred", "Clever", "Clouded", "Cold", "Colossal",
    "Cosmic", "Crimson", "Cunning", "Curious", "Dappled", "Dark", "Daring", "Deadly", "Deep",
    "Distant", "Dull", "Dusky", "Earnest", "Electric", "Emerald", "Endless", "Enigmatic",
    "Ethereal", "Faded", "Faint", "Fallen", "Feral", "Fierce", "Final", "Flawed", "Fractured",
    "Frozen", "Gentle", "Gilded", "Glacial", "Golden", "Grand", "Gray", "Grim", "Harsh", "Hidden",
    "Hollow", "Honed", "Icy", "Idle", "Infernal", "Iron", "Jagged", "Keen", "Last", "Liminal",
    "Lone", "Lucid", "Luminous", "Midnight", "Mighty", "Misty", "Oblique", "Obsidian", "Pale",
    "Phantom", "Polished", "Prime", "Quiet", "Radiant", "Rapid", "Rare", "Ravenous", "Resolute",
    "Scarlet", "Secret", "Shattered", "Silent", "Silver", "Solitary", "Stark", "Steadfast",
    "Stolen", "Strange", "Subtle", "Tenebrous", "Tenacious", "Verdant", "Vigilant", "Violet",
    "Wandering", "Withered", "Wry"
]

NOUNS = [
    "Aegis", "Algorithm", "Alloy", "Apex", "Archive", "Ark", "Aspect", "Atlas", "Aurora", "Beacon",
    "Bastion", "Cipher", "Circuit", "Citadel", "Code", "Comet", "Conduit", "Core", "Crest",
    "Crucible", "Current", "Cycle", "Data", "Dawn", "Depth", "Dominion", "Echo", "Edge", "Ember",
    "Epoch", "Equinox", "Essence", "Ether", "Expanse", "Factor", "Flame", "Flux", "Forge", "Fractal",
    "Frontier", "Frost", "Gate", "Genesis", "Glyph", "Halo", "Haven", "Horizon", "Icon", "Insight",
    "Keystone", "Labyrinth", "Lantern", "Legacy", "Lattice", "Ledger", "Lens", "Loom", "Matrix",
    "Meridian", "Monolith", "Nexus", "Node", "Nova", "Obelisk", "Omen", "Orbit", "Origin",
    "Palisade", "Paradox", "Path", "Pattern", "Peak", "Prism", "Pulse", "Pyre", "Quanta", "Quorum",
    "Realm", "Reliquary", "Reservoir", "Rift", "Runestone", "Sanctuary", "Scribe", "Sentinel",
    "Shard", "Signal", "Spark", "Spectrum", "Spiral", "Spire", "Storm", "Summit", "Tesseract",
    "Threshold", "Titan", "Tome", "Tower", "Trace", "Vector", "Vault", "Veil", "Vortex", "Whisper"
]

def generate_name():
    return f"{random.choice(ADJECTIVES)} {random.choice(NOUNS)}"

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate internal project names (Adjective + Noun)."
    )
    parser.add_argument("-n", "--num", type=int, default=1,
                        help="Number of names to generate")
    args = parser.parse_args()

    for _ in range(args.num):
        print(generate_name())
