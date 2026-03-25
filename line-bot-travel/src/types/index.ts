export interface ChatMessage {
  role: 'user' | 'model'
  content: string
}

export interface ItineraryCache {
  data: string
  fetchedAt: number
}
