# QUICK REFERENCE: Audio Setup
## Isha's Narration - 2 Parts

---

## 📊 **Audio Division**

```
┌─────────────────────────────────────────────────────────────┐
│                    PART 1 (~7 minutes)                      │
│  File: isha_narration_part1.mp3                            │
├─────────────────────────────────────────────────────────────┤
│  Slide 1  │ Executive Summary              │ 0:00 - 0:50  │
│  Slide 2  │ Market Opportunity             │ 0:50 - 1:45  │
│  Slide 3  │ The Challenge                  │ 1:45 - 2:45  │
│  Slide 4  │ The Solution                   │ 2:45 - 3:40  │
│  Slide 5  │ The Science                    │ 3:40 - 4:45  │
│  Slide 6  │ Complete Portfolio             │ 4:45 - 6:00  │
│  Slide 7  │ Flexible Delivery Formats      │ 6:00 - 7:00  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    PART 2 (~5 minutes)                      │
│  File: isha_narration_part2.mp3                            │
├─────────────────────────────────────────────────────────────┤
│  Slide 8  │ Partnership Model              │ 0:00 - 0:50  │
│  Slide 9  │ 1:1 Batch Pricing             │ 0:50 - 2:05  │
│  Slide 10 │ Group Batch Pricing            │ 2:05 - 2:50  │
│  Slide 11 │ Why Partner With Us            │ 2:50 - 3:45  │
│  Slide 12 │ Success Stories                │ 3:45 - 4:30  │
│  Slide 13 │ Call to Action                 │ 4:30 - 5:10  │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 **File Structure**

```
New folder/
│
├── index.html                              ← Your presentation
├── audio/                                  ← CREATE THIS FOLDER
│   ├── isha_narration_part1.mp3           ← Record from Part 1 script
│   └── isha_narration_part2.mp3           ← Record from Part 2 script
│
├── audio_script_part1_isha.md             ← Script for recording Part 1
├── audio_script_part2_isha.md             ← Script for recording Part 2
└── AUDIO_INTEGRATION_GUIDE.md             ← How to add audio to HTML
```

---

## 🎬 **3-Step Setup**

### **STEP 1: Record Audio**
```
✓ Open: audio_script_part1_isha.md
✓ Record: Slides 1-7 narration (~7 min)
✓ Save as: isha_narration_part1.mp3

✓ Open: audio_script_part2_isha.md
✓ Record: Slides 8-13 narration (~5 min)
✓ Save as: isha_narration_part2.mp3
```

### **STEP 2: Create Folder & Add Files**
```bash
# Create audio folder
mkdir audio

# Move your recorded MP3 files into audio folder
# Final structure:
#   audio/isha_narration_part1.mp3
#   audio/isha_narration_part2.mp3
```

### **STEP 3: Add Code to HTML**
```
✓ Open: AUDIO_INTEGRATION_GUIDE.md
✓ Copy: The "Quick Copy-Paste Code" section
✓ Paste: Before </body> tag in index.html
✓ Save: index.html
```

---

## 🎯 **Where Audio Plays**

```
PRESENTATION FLOW:
═══════════════════════════════════════════════════════════

Slide 1  ┐
Slide 2  │
Slide 3  │  ← PART 1 AUDIO PLAYS HERE
Slide 4  │     (isha_narration_part1.mp3)
Slide 5  │
Slide 6  │
Slide 7  ┘

Slide 8  ┐
Slide 9  │
Slide 10 │  ← PART 2 AUDIO PLAYS HERE
Slide 11 │     (isha_narration_part2.mp3)
Slide 12 │
Slide 13 ┘
```

---

## 💡 **What You'll See**

After adding the code, a control panel will appear in the bottom-right:

```
┌──────────────────────────────────┐
│  🎙️ Isha's Narration            │
├──────────────────────────────────┤
│  📍 Part 1: Slides 1-7           │
│  [▶️ ━━━━━━━━━━━━━━━ 🔊]        │
│  Introduction & Offerings (~7min)│
├──────────────────────────────────┤
│  📍 Part 2: Slides 8-13          │
│  [▶️ ━━━━━━━━━━━━━━━ 🔊]        │
│  Commercials & Partnership (~5min)│
└──────────────────────────────────┘
```

---

## ✅ **Quick Checklist**

**Before Recording:**
- [ ] Read through both script files
- [ ] Practice difficult pronunciations
- [ ] Set up quiet recording space
- [ ] Test microphone quality

**During Recording:**
- [ ] Record Part 1 (7 minutes)
- [ ] Take 2-minute break
- [ ] Record Part 2 (5 minutes)
- [ ] Listen to both recordings

**After Recording:**
- [ ] Export as MP3 (128-192 kbps)
- [ ] Name files correctly
- [ ] Create `audio/` folder
- [ ] Move MP3 files to folder
- [ ] Add HTML code
- [ ] Test in browser

---

## 🎤 **Recording Tips**

**Environment:**
- Quiet room (no background noise)
- Close windows (avoid traffic sounds)
- Turn off fans/AC during recording
- Use good quality microphone

**Voice:**
- Warm up voice before recording
- Keep water nearby
- Smile while speaking (it shows in voice!)
- Maintain consistent distance from mic

**Quality:**
- Record in WAV first (high quality)
- Export to MP3 (for web use)
- Keep original WAV as backup
- Bitrate: 128-192 kbps for MP3

---

## 📞 **Need Help?**

**Common Issues:**

❌ **Audio not playing?**
→ Check file names match exactly
→ Verify files are in `audio/` folder
→ Check browser console for errors

❌ **Audio controls not showing?**
→ Verify code is before `</body>` tag
→ Clear browser cache and refresh
→ Check for JavaScript errors

❌ **Audio quality poor?**
→ Re-record with better microphone
→ Use noise reduction in audio editor
→ Export at higher bitrate (192 kbps)

---

## 📚 **All Your Files**

1. ✅ `audio_script_part1_isha.md` - Part 1 recording script
2. ✅ `audio_script_part2_isha.md` - Part 2 recording script  
3. ✅ `AUDIO_INTEGRATION_GUIDE.md` - Detailed integration guide
4. ✅ `presentation_audio_script_hinglish.md` - Complete script (reference)
5. ✅ `slides_summary_reference_hinglish.md` - Quick reference

---

**Ready to Record?** 
Start with `audio_script_part1_isha.md` → Record → Export → Repeat for Part 2 → Integrate!

**Total Time Needed:**
- Recording: ~30-45 minutes (with retakes)
- Editing/Export: ~15 minutes
- Integration: ~5 minutes
- **Total: ~1 hour**

Good luck! 🎙️✨
