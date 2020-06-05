<template>
    <div class="container m-8">
        <div class="text-center">
            <div>
                <button @click="toggleSound()"> 
                    <img v-if="sound.play" :src="this.$attrs.icon + '.svg'" width="50px">
                    <img v-else :src="this.$attrs.icon + '-noplay.svg'" width="50px">
                </button>
            </div>
            <div>
                <input type="range" min="1" max="100" value="50" v-model="sound.volume">
            </div>
        </div>
    </div>
</template>

<script>
import { EventBus } from '../app.js';
    export default {
        mounted(){
            this.sound.audio = new Audio(this.$attrs.file); 
            let vueObj = this
            EventBus.$on(`play-${this.$attrs.label}-volume`, function(volume){
                console.log("should now play sound", vueObj.sound, volume)
                vueObj.play(volume)
            })
            EventBus.$on("adjust-volume", function(volume){
                console.log('adjust volume to', volume)
                vueObj.sound.volume = volume
                if (volume == 0) {
                    vueObj.sound.play = false
                }
            })
        },
        data: function () {
            return {
                sound: {
                    play: false,
                    audio: null,
                    volume: 0
                }
            }
        },
        watch: {
            sound: {
                handler() {
                    this.sound.audio.volume = this.sound.volume / 100
                },
                deep: true
            }
        },
        methods: {
            play(volume=100) {
                this.sound.play = true
                this.sound.volume = volume
                this.sound.audio.loop = true
                this.sound.audio.play()
            },
            toggleSound () {1
                if (this.sound.play) {
                    console.log('pause sound')
                    return this.pause()
                } else {
                    console.log('play sound')
                    return this.play()
                }

                // let event = {
                //     "sounds": [
                //         {
                //             "label": "fire",
                //             "volume": 20
                //         }
                //     ]
                // }
                // let sound;

                // for (sound of event.sounds) {
                //     console.log(sound)
                //     EventBus.$emit(`play-${sound.label}-volume`, sound.volume)
                // }
            },
            pauseSound () {
                this.sound.play = false
                this.sound.volume = 0
                this.sound.audio.pause();  
            },
            pause () {
                this.sound.play = false
                this.sound.audio.pause();  
            }
        }
    }
</script>