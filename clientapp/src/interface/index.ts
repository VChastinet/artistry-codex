export interface ServerResponse {
  results: any;
  count: number;
  next: string;
  previous: string;
}

export interface Artist {
  name: string;
  id: number;
  contact: string;
  portfolio: string;
  state: State;
  instagram_username: string;
  tags: Tag[];
}

export interface Tag {
  id: number;
  name: string;
  description?: string;
}

export interface State {
  id: number;
  uf: string;
  name: string;
}
