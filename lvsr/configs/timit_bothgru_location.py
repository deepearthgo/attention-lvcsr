Config(
    net=Config(dec_transition='GatedRecurrent',
               enc_transition='GatedRecurrent',
               rec_weights_init='IsotropicGaussian(0.1)',
               attention_type='location',
               shift_predictor_dims=[100],
               max_left=10,
               max_right=100),
    data=Config(normalization="norm.pkl"))
