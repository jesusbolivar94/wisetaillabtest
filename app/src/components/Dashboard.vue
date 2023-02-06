<script setup>
    import { onMounted } from 'vue'
    import Chart from 'chart.js/auto'
    import data from '../../../data.json'

    onMounted(() => {
        const canvas = document.querySelector('#stats')

        new Chart(
            canvas,
            {
                type: 'line',
                data: {
                    labels: Object.keys(data),
                    datasets: [
                        {
                            label: 'MCoutinho Peças',
                            data: Object.values(data),
                        }
                    ],
                },
                options: {
                    scales: {
                        y: {
                            min: Math.min( ...Object.values(data) ),
                            max: Math.max( ...Object.values(data) ),
                        }
                    }
                }
            }
        )
    })
</script>

<template>
    <h1 class="font-bold text-3xl">Wise Tail Lab Test</h1>
    <div class="w-9/12">
        <canvas id="stats"></canvas>
    </div>
</template>