import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    // Allow access via Tailscale MagicDNS names (and *.local) when serving
    // with `--remote`. A leading dot allows all subdomains of that domain.
    allowedHosts: ['.ts.net', '.local'],
  },
})
