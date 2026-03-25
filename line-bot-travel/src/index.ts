import 'dotenv/config'
import { serve } from '@hono/node-server'
import { Hono } from 'hono'
import { webhookRoute } from './routes/webhook.js'

const app = new Hono()

app.get('/health', (c) => c.json({ status: 'ok' }))
app.route('/webhook', webhookRoute)

const port = Number(process.env.PORT) || 8080

serve({ fetch: app.fetch, port }, () => {
  console.log(`Server running on port ${port}`)
})
