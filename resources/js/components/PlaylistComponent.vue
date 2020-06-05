<template>
    <div>
        <div @click="play('Camping')"> Camping </div>
        <div @click="play('Calm in a car')"> Calm in a car </div>
        <div @click="play('Driving at night in the rain')"> Driving at night in the rain </div>
        <div @click="play('Summer Day')"> Summer Day </div>
        <div @click="mute()"> Mute </div>
    </div>
</template>

<script>
import { EventBus } from '../app.js';
export default {
    data() {
        return {
            'playlists': {
                'Camping': [
                    {"label": "fire", "volume": 20},
                    {"label": "rain", "volume": 60},
                    {"label": "night", "volume": 60},
                    {"label": "thunder", "volume": 40},
                    {"label": "cicada", "volume": 5},
                ],
                'Calm in a car': [
                    {"label": "rain", "volume": 30},
                    {"label": "car-rain", "volume": 100},
                    {"label": "thunder", "volume": 70},
                    {"label": "cicada", "volume": 5},
                    {"label": "night", "volume": 45},
                ],
                'Driving at night in the rain': [
                    {"label": "car-rain", "volume": 100},
                    {"label": "car", "volume": 30},
                    {"label": "thunder", "volume": 60},
                    {"label": "night", "volume": 30},
                ],
                'Summer Day': [
                    {"label": "air-conditioner", "volume": 100},
                    {"label": "lawnmower", "volume": 30},
                    {"label": "bird", "volume": 50},
                ],
            }
        }
    },
    methods: {
        play(playlist){
            this.mute()

            let sound; 
            for (sound of this.playlists[playlist]) {
                console.log(sound)
                EventBus.$emit(`play-${sound.label}-volume`, sound.volume)
            }
        },
        mute(playlist){
            EventBus.$emit("adjust-volume", 0)
        }
    }
}
</script>