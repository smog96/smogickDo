import { Dispatch, SetStateAction } from "react";

export type Nullable<T> = T | null;
export type SetState<T> = Dispatch<SetStateAction<T>>;
