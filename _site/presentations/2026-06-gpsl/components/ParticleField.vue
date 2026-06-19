<template>
  <canvas ref="canvasRef" class="particle-field" />
</template>

<script setup>
import { onMounted, onBeforeUnmount, ref } from 'vue'

const canvasRef = ref(null)
let rafId = null
let onMouseMove = null
let onResize = null

onMounted(() => {
  const canvas = canvasRef.value
  const ctx = canvas.getContext('2d')

  let width, height, particles
  const mouse = { x: 0, y: 0 }

  function init() {
    const rect = canvas.getBoundingClientRect()
    width = canvas.width = rect.width
    height = canvas.height = rect.height
    mouse.x = width / 2
    mouse.y = height / 2

    const numParticles = Math.floor((width * height) / 12000)
    particles = []
    for (let i = 0; i < numParticles; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.5,
        vy: (Math.random() - 0.5) * 0.5,
        radius: Math.random() * 1.5 + 0.5,
      })
    }
  }

  function animate() {
    ctx.clearRect(0, 0, width, height)

    const grad = ctx.createRadialGradient(mouse.x, mouse.y, 0, mouse.x, mouse.y, 400)
    grad.addColorStop(0, 'rgba(94, 129, 172, 0.06)')
    grad.addColorStop(1, 'rgba(0, 0, 0, 0)')
    ctx.fillStyle = grad
    ctx.fillRect(0, 0, width, height)

    for (let i = 0; i < particles.length; i++) {
      const p = particles[i]
      p.x += p.vx
      p.y += p.vy
      if (p.x < 0 || p.x > width) p.vx *= -1
      if (p.y < 0 || p.y > height) p.vy *= -1

      ctx.beginPath()
      ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2)
      ctx.fillStyle = 'rgba(59, 66, 82, 0.55)'
      ctx.fill()

      for (let j = i + 1; j < particles.length; j++) {
        const p2 = particles[j]
        const dx = p.x - p2.x
        const dy = p.y - p2.y
        const dist = Math.sqrt(dx * dx + dy * dy)
        if (dist < 120) {
          ctx.beginPath()
          ctx.moveTo(p.x, p.y)
          ctx.lineTo(p2.x, p2.y)
          ctx.strokeStyle = `rgba(59, 66, 82, ${0.22 * (1 - dist / 120)})`
          ctx.lineWidth = 0.6
          ctx.stroke()
        }
      }

      const mx = p.x - mouse.x
      const my = p.y - mouse.y
      const mouseDist = Math.sqrt(mx * mx + my * my)
      if (mouseDist < 200) {
        ctx.beginPath()
        ctx.moveTo(p.x, p.y)
        ctx.lineTo(mouse.x, mouse.y)
        ctx.strokeStyle = `rgba(94, 129, 172, ${0.55 * (1 - mouseDist / 200)})`
        ctx.lineWidth = 1
        ctx.stroke()
        p.vx += (mouse.x - p.x) * 0.00005
        p.vy += (mouse.y - p.y) * 0.00005
      }
    }

    rafId = requestAnimationFrame(animate)
  }

  onMouseMove = (e) => {
    const rect = canvas.getBoundingClientRect()
    mouse.x = e.clientX - rect.left
    mouse.y = e.clientY - rect.top
  }
  onResize = () => init()

  window.addEventListener('mousemove', onMouseMove)
  window.addEventListener('resize', onResize)

  init()
  animate()
})

onBeforeUnmount(() => {
  if (rafId) cancelAnimationFrame(rafId)
  if (onMouseMove) window.removeEventListener('mousemove', onMouseMove)
  if (onResize) window.removeEventListener('resize', onResize)
})
</script>

<style scoped>
.particle-field {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
}
</style>
