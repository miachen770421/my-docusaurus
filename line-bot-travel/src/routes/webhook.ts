import { Hono } from 'hono'

export const webhookRoute = new Hono()

webhookRoute.post('/', async (c) => {
  // Phase 2 實作
  return c.text('OK', 200)
})
