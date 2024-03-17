import type { IProducts } from "../interfaces/produtos";

export const useCart = () => useState<IProducts[]>('cart', () => []);

export const usePrice = () => useState<number>('price', () => 0);