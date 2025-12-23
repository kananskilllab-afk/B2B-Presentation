# Audio Integration Guide
## How to Add Audio to Your Presentation

---

## 📁 **Audio Files Structure**

After recording, you should have these files:

```
New folder/
├── index.html
├── audio/
│   ├── isha_narration_part1.mp3  (Slides 1-7, ~6-7 minutes)
│   └── isha_narration_part2.mp3  (Slides 8-13, ~5-6 minutes)
```

---

## 🎯 **Audio Division Summary**

### **PART 1: Introduction & Offerings** (Slides 1-7)
**Duration**: ~6-7 minutes  
**File**: `isha_narration_part1.mp3`

**Covers:**
- Slide 1: Executive Summary / Cover
- Slide 2: Market Opportunity
- Slide 3: The Challenge
- Slide 4: The Solution
- Slide 5: The Science
- Slide 6: Complete Portfolio
- Slide 7: Flexible Delivery Formats

**Content Focus**: Introduction, problem-solution, scientific backing, course offerings

---

### **PART 2: Commercials & Partnership** (Slides 8-13)
**Duration**: ~5-6 minutes  
**File**: `isha_narration_part2.mp3`

**Covers:**
- Slide 8: Partnership Model
- Slide 9: 1:1 Batch Pricing
- Slide 10: Group Batch Pricing
- Slide 11: Why Partner With Us
- Slide 12: Success Stories
- Slide 13: Call to Action

**Content Focus**: Partnership details, pricing, benefits, closing

---

## 💻 **How to Add Audio to HTML**

### **Option 1: Auto-Play Audio on Slide Navigation (Recommended)**

Add this code to your `index.html` before the closing `</body>` tag:

```html
<!-- Audio Players -->
<audio id="audio-part1" preload="auto">
    <source src="audio/isha_narration_part1.mp3" type="audio/mpeg">
    Your browser does not support the audio element.
</audio>

<audio id="audio-part2" preload="auto">
    <source src="audio/isha_narration_part2.mp3" type="audio/mpeg">
    Your browser does not support the audio element.
</audio>

<!-- Audio Control Script -->
<script>
    const audioPart1 = document.getElementById('audio-part1');
    const audioPart2 = document.getElementById('audio-part2');
    let currentAudio = null;

    // Function to play audio based on slide number
    function playAudioForSlide(slideIndex) {
        // Stop any currently playing audio
        if (currentAudio) {
            currentAudio.pause();
            currentAudio.currentTime = 0;
        }

        // Play appropriate audio based on slide
        if (slideIndex >= 0 && slideIndex <= 6) {
            // Slides 1-7 (index 0-6)
            currentAudio = audioPart1;
            
            // Calculate time offset for specific slide
            const slideTimings = [0, 50, 105, 165, 220, 285, 360]; // Start times in seconds
            if (slideTimings[slideIndex] !== undefined) {
                audioPart1.currentTime = slideTimings[slideIndex];
            }
            audioPart1.play();
        } else if (slideIndex >= 7 && slideIndex <= 12) {
            // Slides 8-13 (index 7-12)
            currentAudio = audioPart2;
            
            // Calculate time offset for specific slide
            const slideTimings = [0, 50, 125, 170, 225, 270]; // Start times in seconds
            const adjustedIndex = slideIndex - 7;
            if (slideTimings[adjustedIndex] !== undefined) {
                audioPart2.currentTime = slideTimings[adjustedIndex];
            }
            audioPart2.play();
        }
    }

    // Add to your existing slide navigation code
    // Call playAudioForSlide(currentSlideIndex) when slide changes
</script>
```

---

### **Option 2: Manual Audio Controls (User-Controlled)**

Add audio controls that users can play/pause:

```html
<!-- Audio Control Panel -->
<div style="position: fixed; bottom: 100px; right: 20px; z-index: 1000; background: rgba(255,255,255,0.9); padding: 1rem; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
    <div style="margin-bottom: 0.5rem; font-weight: 600; color: #1e293b;">
        🎙️ Isha's Narration
    </div>
    
    <!-- Part 1 Controls -->
    <div style="margin-bottom: 0.5rem;">
        <div style="font-size: 0.85rem; color: #64748b; margin-bottom: 0.25rem;">
            Part 1 (Slides 1-7)
        </div>
        <audio controls style="width: 100%; height: 30px;">
            <source src="audio/isha_narration_part1.mp3" type="audio/mpeg">
        </audio>
    </div>
    
    <!-- Part 2 Controls -->
    <div>
        <div style="font-size: 0.85rem; color: #64748b; margin-bottom: 0.25rem;">
            Part 2 (Slides 8-13)
        </div>
        <audio controls style="width: 100%; height: 30px;">
            <source src="audio/isha_narration_part2.mp3" type="audio/mpeg">
        </audio>
    </div>
</div>
```

---

### **Option 3: Individual Slide Audio (Most Control)**

If you want to record separate audio for each slide:

```html
<!-- Individual Slide Audios -->
<audio id="slide1-audio" src="audio/slide1.mp3" preload="auto"></audio>
<audio id="slide2-audio" src="audio/slide2.mp3" preload="auto"></audio>
<!-- ... etc for all slides -->

<script>
    function playSlideAudio(slideNumber) {
        // Stop all audios
        document.querySelectorAll('audio').forEach(audio => {
            audio.pause();
            audio.currentTime = 0;
        });
        
        // Play current slide audio
        const audio = document.getElementById(`slide${slideNumber}-audio`);
        if (audio) {
            audio.play();
        }
    }
</script>
```

---

## 🎬 **Integration Steps**

### **Step 1: Create Audio Folder**
```bash
# In your project folder
mkdir audio
```

### **Step 2: Record & Export Audio**
1. Record Part 1 using `audio_script_part1_isha.md`
2. Record Part 2 using `audio_script_part2_isha.md`
3. Export as MP3 files:
   - `isha_narration_part1.mp3`
   - `isha_narration_part2.mp3`

### **Step 3: Place Audio Files**
Move the MP3 files to the `audio` folder:
```
New folder/
├── audio/
│   ├── isha_narration_part1.mp3
│   └── isha_narration_part2.mp3
```

### **Step 4: Add HTML Code**
Choose one of the options above and add the code to your `index.html`

### **Step 5: Test**
1. Open `index.html` in browser
2. Navigate through slides
3. Verify audio plays correctly

---

## ⏱️ **Slide Timing Reference**

### **Part 1 Timings** (isha_narration_part1.mp3)
| Slide | Start Time | Duration | Content |
|-------|-----------|----------|---------|
| 1 | 0:00 | 0:50 | Executive Summary |
| 2 | 0:50 | 0:55 | Market Opportunity |
| 3 | 1:45 | 1:00 | The Challenge |
| 4 | 2:45 | 0:55 | The Solution |
| 5 | 3:40 | 1:05 | The Science |
| 6 | 4:45 | 1:15 | Complete Portfolio |
| 7 | 6:00 | 1:00 | Delivery Formats |

**Total**: ~7:00 minutes

---

### **Part 2 Timings** (isha_narration_part2.mp3)
| Slide | Start Time | Duration | Content |
|-------|-----------|----------|---------|
| 8 | 0:00 | 0:50 | Partnership Model |
| 9 | 0:50 | 1:15 | 1:1 Pricing |
| 10 | 2:05 | 0:45 | Group Pricing |
| 11 | 2:50 | 0:55 | Why Partner |
| 12 | 3:45 | 0:45 | Success Stories |
| 13 | 4:30 | 0:40 | Call to Action |

**Total**: ~5:10 minutes

---

## 🎨 **Recommended Implementation**

For your B2B presentation, I recommend **Option 2** (Manual Controls) because:

✅ **Professional**: Gives viewers control over audio  
✅ **Flexible**: Can pause/replay as needed  
✅ **User-Friendly**: Clear visual controls  
✅ **Non-Intrusive**: Doesn't auto-play unexpectedly  

---

## 📝 **Quick Copy-Paste Code**

Here's the complete code to add to your `index.html`:

```html
<!-- Add this before closing </body> tag -->

<!-- Audio Control Panel -->
<div id="audio-control-panel" style="position: fixed; bottom: 100px; right: 20px; z-index: 1000; background: rgba(255,255,255,0.95); padding: 1.25rem; border-radius: 16px; box-shadow: 0 8px 24px rgba(0,0,0,0.12); backdrop-filter: blur(10px); min-width: 280px;">
    <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem; font-weight: 700; color: #1e293b; font-size: 1.1rem;">
        <i class="fas fa-microphone" style="color: #4f46e5;"></i>
        Isha's Narration
    </div>
    
    <!-- Part 1 Controls -->
    <div style="margin-bottom: 1rem; padding: 0.75rem; background: #f8fafc; border-radius: 8px;">
        <div style="font-size: 0.9rem; color: #64748b; margin-bottom: 0.5rem; font-weight: 600;">
            📍 Part 1: Slides 1-7
        </div>
        <audio controls style="width: 100%; height: 32px;">
            <source src="audio/isha_narration_part1.mp3" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
        <div style="font-size: 0.75rem; color: #94a3b8; margin-top: 0.25rem;">
            Introduction & Offerings (~7 min)
        </div>
    </div>
    
    <!-- Part 2 Controls -->
    <div style="padding: 0.75rem; background: #f8fafc; border-radius: 8px;">
        <div style="font-size: 0.9rem; color: #64748b; margin-bottom: 0.5rem; font-weight: 600;">
            📍 Part 2: Slides 8-13
        </div>
        <audio controls style="width: 100%; height: 32px;">
            <source src="audio/isha_narration_part2.mp3" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
        <div style="font-size: 0.75rem; color: #94a3b8; margin-top: 0.25rem;">
            Commercials & Partnership (~5 min)
        </div>
    </div>
    
    <!-- Toggle Button -->
    <button onclick="document.getElementById('audio-control-panel').style.display='none'" 
            style="position: absolute; top: 8px; right: 8px; background: transparent; border: none; color: #94a3b8; cursor: pointer; font-size: 1.2rem; padding: 4px;">
        <i class="fas fa-times"></i>
    </button>
</div>

<!-- Show Audio Button (if panel is hidden) -->
<button id="show-audio-btn" onclick="document.getElementById('audio-control-panel').style.display='block'; this.style.display='none';" 
        style="display: none; position: fixed; bottom: 100px; right: 20px; z-index: 999; background: #4f46e5; color: white; border: none; padding: 0.75rem 1rem; border-radius: 50px; cursor: pointer; box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3); font-weight: 600;">
    <i class="fas fa-microphone"></i> Show Audio
</button>
```

---

## ✅ **Testing Checklist**

- [ ] Audio files are in `audio/` folder
- [ ] File names match exactly: `isha_narration_part1.mp3` and `isha_narration_part2.mp3`
- [ ] HTML code is added before `</body>` tag
- [ ] Audio controls appear on the page
- [ ] Part 1 plays correctly for slides 1-7
- [ ] Part 2 plays correctly for slides 8-13
- [ ] Audio quality is clear
- [ ] Volume levels are consistent between parts
- [ ] Play/pause controls work properly

---

## 🎯 **Best Practices**

1. **File Size**: Keep MP3 files under 10MB each for faster loading
2. **Quality**: Use 128-192 kbps bitrate for good quality
3. **Format**: MP3 is universally supported
4. **Backup**: Keep original WAV/high-quality files as backup
5. **Testing**: Test on multiple browsers (Chrome, Firefox, Safari)

---

**Created**: December 23, 2025  
**For**: Kanan.co B2B Presentation  
**Narrator**: Isha  
**Total Duration**: ~12 minutes (Part 1: 7 min, Part 2: 5 min)
