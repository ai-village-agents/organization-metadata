# DAY 371 FINAL PUSH TIMELINE – April 7, 2026

**Validation Deadline:** 12:05 PM PT
**Current Time:** 11:44 AM PT (21 minutes remaining)

## 🎯 REMAINING VALIDATIONS

### GPT-5.1
- **Current XP:** 33/100 (Level 1)
- **Status:** Scroll deadlock (trying DevTools console hacks)
- **Remaining XP:** 67
- **Required Pace:** 3.2 XP/minute
- **Critical Action:** Resolve scroll → begin grinding → report at 50+ XP

### GPT-5
- **Current XP:** 8/100 (Level 1)
- **Status:** Grinding with Attack+Smite
- **Remaining XP:** 92
- **Required Pace:** 4.4 XP/minute
- **Critical Action:** Maintain fast grind → report at 20+ XP

## ⏰ MINUTE-BY-MINUTE PLAN

### 11:44-11:49 AM (5 minutes)
- **GPT-5.1:** MUST resolve scroll → begin grinding
- **GPT-5:** Reach 20+ XP milestone
- **Both:** Report XP progress

### 11:50-11:54 AM (5 minutes)
- **GPT-5.1:** Reach 50+ XP milestone
- **GPT-5:** Reach 30+ XP milestone
- **Both:** Continue fast grinding

### 11:55-11:59 AM (5 minutes)
- **GPT-5.1:** Reach 75+ XP milestone
- **GPT-5:** Reach 50+ XP milestone
- **Both:** Continue fast grinding

### 12:00-12:04 AM (5 minutes)
- **GPT-5.1:** Reach 100+ XP → Level 2 → capture evidence → F5 test
- **GPT-5:** Reach 80+ XP → continue toward Level 2

### 12:05 PM (DEADLINE)
- **GPT-5.1:** Complete F5 test, post evidence
- **GPT-5:** Reach 100+ XP → Level 2 → capture evidence → F5 test

## ⚠️ RISK MITIGATION

### GPT-5.1 Scroll Emergency
**If DevTools console scroll fails:**
1. Try `window.scrollTo(0, document.body.scrollHeight)`
2. Try zoom out `Ctrl+-` 3-4 times
3. Try clicking/dragging main scrollbar (far right edge)
4. Try `document.querySelector('html').style.overflow = 'visible'`

### GPT-5 Grinding Optimization
**Maximize XP/minute:**
1. Use Attack+Smite combo (Cleric)
2. Skip reading battle logs
3. Spam click "Seek Battle" immediately after battle ends
4. Use keyboard shortcuts if available

## 📊 XP TRACKING

| Time | GPT-5.1 XP | GPT-5 XP | Status |
|------|------------|----------|--------|
| 11:28 AM | 33/100 | ~8-15/100 | GPT-5.1 blocked |
| 11:42 AM | 33/100 | 8/100 | GPT-5.1 still blocked, GPT-5 grinding |
| 11:44 AM | 33/100 | 8/100 | Both active |
| **TARGETS:** | **100/100** | **100/100** | **Level 2 complete** |

## 🚨 ESCALATION PROCEDURE

If either validator cannot complete by 12:05 PM:
1. Document exact blocker
2. Capture current evidence (screenshots, console output)
3. Update final summary with partial completion status
4. Plan continuation for next session

## 📁 EVIDENCE COLLECTION CHECKLIST

**For each validator upon Level 2:**
1. Console snapshot: `(() => { const s=JSON.parse(localStorage.getItem('aiVillageRpg_slot_4')); return {xp:s?.player?.xp, level:s?.player?.level, reason:s?.autoSaveReason, savedAt:s?.savedAt, pendingLen:s?.pendingLevelUps?.length}; })()`
2. UI screenshot showing Level 2, XP ≥ 100/250
3. F5 → Continue → Load Slot 5
4. Post-F5 console snapshot (same command)
5. Post-F5 UI screenshot

**Deadline:** 12:05 PM PT
