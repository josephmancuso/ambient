<template>
    <div class="container m-8">
        <div class="text-center">
            <div>
                <button @click="playSound()"> 
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
    export default {
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
            playSound () {
                if(this.$attrs.file) {
                    var audio = new Audio(this.$attrs.file); 
                    if (this.sound.play) {
                        return this.pauseSound() 
                    } else {
                        this.sound.volume = 100
                        this.sound.play = true
                        this.sound.audio = audio
                        this.sound.audio.loop = true
                        this.sound.audio.play()

                    }

                }
            },
            pauseSound () {
                this.sound.volume = 0
                this.sound.play = false
                this.sound.audio.pause();  
            }
        }
    }
</script>