import Unit from './Unit';
import { IS_MAINNET } from './constants';

export default {
  [Unit.PIPSCOIN]: IS_MAINNET ? 'PIPS' : 'TPIPS',
};
