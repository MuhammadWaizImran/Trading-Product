"""Copy the source project's intro presentation, never its auth or automation."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path('C:/Users/DELL/Downloads/linkedin automation/public')
web = ROOT/'workbench/web'
html = (web/'chat.html').read_text(encoding='utf-8')
original = (SOURCE/'index.html').read_text(encoding='utf-8-sig')
intro = original[original.index('<section id="startup"'):original.index('<script src="/app.js"')]
intro = intro.replace('ProfileEase', 'Crypto Research').replace('PROFILEEASE', 'CRYPTO RESEARCH')
intro = intro.replace('VOICE CAPTURE', 'PDF LIBRARY').replace('AVAILABLE', 'LOCAL')
intro = intro.replace('LINKEDIN SESSION', 'LIVE AGENTS').replace('MODEL PROVIDER', 'MODEL STATUS').replace('GROQ', 'EVALUATING')
intro = intro.replace('<button id="skip-intro">', '<button id="intro-sound" aria-pressed="false">Sound on</button><button id="skip-intro">')
if 'id="startup"' not in html:
    html = html.replace('<header class="topbar">', '<div id="app-shell" inert><header class="topbar">')
    html = html.replace('<script src="/chat.js">', '</div>'+intro+'<script src="/chat.js">')
    html = html.replace('<section class="recent"', '<button id="replay-intro" class="rail-item">Replay intro</button><section class="recent"')
# Repair damaged non-ASCII glyphs introduced by the previous shell encoding.
html = html.replace('aria-label="Close sidebar">?', 'aria-label="Close sidebar">&times;')
html = html.replace('aria-label="Close dialog">?', 'aria-label="Close dialog">&times;')
html = html.replace('aria-label="Choose a PDF source">?', 'aria-label="Choose a PDF source">+')
html = html.replace('aria-label="Send message">?', 'aria-label="Send message">&uarr;')
html = html.replace('aria-label="More research tools">???', 'aria-label="More research tools">&bull;&bull;&bull;')
html = html.replace('Ask anything ? or', 'Ask anything &hellip; or')
html = html.replace('Search conversations?', 'Search conversations...')
html = html.replace('>See More ?', '>See More &darr;').replace('hidden>? Back', 'hidden>&larr; Back')
html = html.replace('search ? Model', 'search &middot; Model').replace('W ? Waiz', 'W &middot; Waiz')
html = html.replace('>? &nbsp;', '>&#10022; &nbsp;').replace('>? ', '>&#10022; ')
html = html.replace('AI Chat', 'AI Chat')
(web/'chat.html').write_text(html, encoding='utf-8')
sound = (SOURCE/'experience.js').read_text(encoding='utf-8-sig')
sound = sound[sound.index('function playIntroSound()'):sound.index('export function initializeExperience')]
visuals = (web/'visuals.js').read_text(encoding='utf-8')
if 'function playIntroSound()' not in visuals:
    visuals += '\n'+sound+'\n'
    (web/'visuals.js').write_text(visuals, encoding='utf-8')
print('Copied original intro markup and sound synthesis; auth omitted.')
