# Live reference replication — 2026-10-29

Reference: https://7b0d2065-eba3-4772-8643-a00310b676da-00-2xfjfhuqzh7r5.sisko.replit.dev/

Read the publicly served App, IntroScreen, QuantumOrb3D and home components. Snapshots are in research/live-ui-reference. Only selected presentation logic was adapted; no authentication routes, account calls, payment workflow, external model endpoints or remote telemetry were imported.

Implemented: tap gate; source-timed intro/audio sequence; four distinct expanding rings; animated title/lines/status rows/dots; fade; skip/replay/mute; rotating plasma orb with the original double-heartbeat timing; welcome/chat orb sizes; default input styling with optional gold appearance; original suggestion labels; collapsible sidebar/backdrop; searchable browser-local multi-message sessions; edit-to-composer; copy answers; pending/error states; theme presets; voice overlay with explicit microphone start/stop, browser speech-to-text and speech playback; Lens image upload/camera preview/capture with media cleanup.

Authentication is excluded as requested. Checked PDF retrieval remains the only answer backend. Original general-purpose AI chat, image generation, OCR, image interpretation, translation and wake-word background listening are NOT connected. Lens images remain local. Speech recognition can use browser-provider servers and is disclosed before microphone activation. Voice/camera need browser support and user permission. No claim of complete functional parity or exact pixel parity is justified yet.

Validation:13 existing backend tests pass; JS syntax and DOM-selector/unique-ID checks pass;8 mocked intro lifecycle scenarios pass; current HTTP routes return200. Browser preview tooling returned 'browser access host is unavailable', so screenshots, microphone/camera behavior and desktop/mobile rendering remain unverified. Preview http://127.0.0.1:8766/ .
