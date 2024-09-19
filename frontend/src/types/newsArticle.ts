// Define the NewsArticle type representing a news article related to a startup company
export type NewsArticle = {
  // Unique identifier for the news article
  id: number;

  // ID of the startup company associated with this news article
  startup_id: number;

  // Title of the news article
  title: string;

  // URL link to the full news article
  url: string;

  // Date when the article was published
  published_date: Date;
};